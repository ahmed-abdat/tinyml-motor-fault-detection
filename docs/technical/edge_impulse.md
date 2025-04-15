# Edge Impulse Setup Guide for Rotating Machine Fault Detection

This guide provides step-by-step instructions for setting up an Edge Impulse project for rotating machine fault detection and deploying it to the ESP32.

## 1. Project Creation and Data Upload

### Create a New Project

1. Go to [Edge Impulse](https://studio.edgeimpulse.com/)
2. Sign in or create a new account
3. Click "Create new project"
4. Name your project (e.g., "Rotating-Machine-Fault-Detection")
5. Select "Developer" project type
6. Click "Create project"

### Configure Project Settings

1. Go to "Dashboard"
2. Under "Project info" click "Modify"
3. Set the following:
   - Sample frequency (Hz): 1000
   - Sample length (ms): 5000
   - Sensor axes: 3 (X, Y, Z)

### Upload Dataset

#### Using the Web Interface

1. Go to "Data acquisition"
2. Click "Upload data"
3. Select "Upload existing data"
4. Choose the following settings:
   - Data type: Accelerometer data
   - Sample format: CSV
   - Time series: Yes
   - Sample categories: Split between training and testing (80/20)
   - Upload your files from the `dataset_csv` folder (or from the EMD-processed data folder if you've completed preprocessing)

#### Using the Edge Impulse CLI (Alternative)

If you have many files, using the CLI might be more efficient:

1. Install the Edge Impulse CLI:

   ```bash
   npm install -g edge-impulse-cli
   ```

2. Log in:

   ```bash
   edge-impulse-uploader --login
   ```

3. Upload files:

   ```bash
   # For healthy files
   edge-impulse-uploader --category training --label healthy dataset_csv/healthy/*.csv

   # For faulty files
   edge-impulse-uploader --category training --label faulty dataset_csv/faulty/*.csv
   ```

## 2. Create Processing Blocks

### Configure the Impulse

1. Go to "Create impulse"
2. Set the following:
   - Window size: 5000 ms
   - Window increase: 5000 ms
3. Add the following processing blocks:
   - "Spectral Analysis" (for frequency domain features)
   - "Raw Data" (for time domain features)
4. Add "Classification" learning block
5. Click "Save impulse"

### Configure Spectral Analysis

1. Click on "Spectral Analysis"
2. Set the following parameters:
   - Frequency range: 0-500 Hz
   - Frame length: 0.02s
   - Frame stride: 0.01s
3. Click "Save parameters"
4. Click "Generate features"

### Configure Raw Data

1. Click on "Raw Data"
2. Select axes X, Y, and Z
3. Click "Save parameters"
4. Click "Generate features"

## 3. Feature Exploration

1. Go to "Feature explorer"
2. Explore the separation between healthy and faulty classes
3. Note which features provide the best separation
4. You can try dimensionality reduction like PCA or t-SNE to visualize the feature space

## 4. Model Training

### Train Neural Network

1. Click on "NN Classifier"
2. Choose a model architecture:
   - For a simple approach, start with 2-3 dense layers
   - For more complex approach, try 1D CNN architecture
3. Example Configuration:
   ```
   Dense (20 neurons, relu activation)
   Dropout (0.2)
   Dense (10 neurons, relu activation)
   Dense (2 neurons, softmax activation)
   ```
4. Set training parameters:
   - Learning rate: 0.001
   - Number of training cycles: 30
   - Batch size: 32
5. Click "Start training"

### Train SVM (Alternative)

Since the paper found SVM with Gaussian kernel to be effective:

1. Go to "Classification"
2. Click "Switch learning block"
3. Select "K-means Anomaly Detection"
4. Click "Save parameters"
5. Go back to "Classification"
6. Click "Switch learning block" again
7. Select "Transfer Learning (Images)" (This allows custom DSP blocks)
8. Write Custom Processing Block in Expert Mode for SVM:

   ```javascript
   // Create custom SVM block
   const SVM = require("@stdlib/ml-svm");

   // Configure SVM with Gaussian kernel
   const svm = new SVM({
     kernel: "gaussian",
     gamma: 0.5,
     C: 1.0,
   });

   // Train model
   svm.train(features, labels);

   // Test model
   const predictions = svm.predict(testFeatures);
   ```

## 5. Model Testing and Validation

1. Go to "Model testing"
2. Click "Classify all"
3. Review the confusion matrix and performance metrics
4. Adjust model or features if needed to improve performance

## 6. ESP32 Deployment

### Export Model for ESP32

1. Go to "Deployment"
2. Select "Arduino library"
3. Configure settings:
   - Target: ESP32
   - Quantization: Int8 (for smallest model size)
   - Optimization: Balanced or Fast
4. Click "Build"
5. Download the ZIP file

### ESP32 Implementation

1. Extract the downloaded ZIP
2. Open Arduino IDE
3. Install ESP32 board support if not already installed
4. Go to Sketch > Include Library > Add .ZIP Library
5. Select the extracted folder
6. Use the example code as a starting point:

```cpp
#include <RotatingMachineFaultDetection_inferencing.h>
#include <Wire.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>

Adafruit_MPU6050 mpu;

// Buffer to store accelerometer data
float features[EI_CLASSIFIER_DSP_INPUT_FRAME_SIZE];
size_t feature_ix = 0;

void setup() {
    Serial.begin(115200);
    while (!Serial) {
        delay(10);
    }

    // Initialize accelerometer
    if (!mpu.begin()) {
        Serial.println("Failed to find MPU6050 sensor!");
        while (1) {
            delay(10);
        }
    }

    // Set up accelerometer
    mpu.setAccelerometerRange(MPU6050_RANGE_8_G);

    Serial.println("Rotating Machine Fault Detection");
    Serial.println("--------------------------------");
}

void loop() {
    // Get new sensor reading
    sensors_event_t a, g, temp;
    mpu.getEvent(&a, &g, &temp);

    // Add data to buffer
    features[feature_ix++] = a.acceleration.x;
    features[feature_ix++] = a.acceleration.y;
    features[feature_ix++] = a.acceleration.z;

    // Buffer filled? Then classify
    if (feature_ix == EI_CLASSIFIER_DSP_INPUT_FRAME_SIZE) {
        Serial.println("Running inference...");

        // Run inference
        ei_impulse_result_t result;
        signal_t signal;

        numpy::signal_from_buffer(features, EI_CLASSIFIER_DSP_INPUT_FRAME_SIZE, &signal);

        EI_IMPULSE_ERROR res = run_classifier(&signal, &result, false);
        if (res != 0) return;

        // Print predictions
        Serial.println("Predictions:");
        for (size_t ix = 0; ix < EI_CLASSIFIER_LABEL_COUNT; ix++) {
            Serial.print("    ");
            Serial.print(result.classification[ix].label);
            Serial.print(": ");
            Serial.println(result.classification[ix].value);
        }

        // Get prediction - highest confidence class
        float max_value = 0;
        size_t max_ix = 0;
        for (size_t ix = 0; ix < EI_CLASSIFIER_LABEL_COUNT; ix++) {
            if (result.classification[ix].value > max_value) {
                max_value = result.classification[ix].value;
                max_ix = ix;
            }
        }

        // Output prediction
        if (max_value > 0.7) {  // Confidence threshold
            if (max_ix == 0) {
                Serial.println("ALERT: Machine fault detected!");
                // Add your fault response here (e.g., LED, alert, etc.)
            } else {
                Serial.println("Machine status: Healthy");
            }
        } else {
            Serial.println("Uncertain prediction, continue monitoring");
        }

        // Reset buffer
        feature_ix = 0;
    }

    delay(10); // Sample at ~100 Hz
}
```

## 7. Next Steps

1. **Optimize for Real-time Operation**:

   - Implement a sliding window approach for continuous monitoring
   - Add power management features
   - Consider increasing sampling frequency for critical applications

2. **Enhance the ESP32 Implementation**:

   - Add LED indicators or display for status
   - Implement WiFi connectivity to send alerts
   - Add data logging to SD card

3. **Evaluate in Real-world Conditions**:
   - Test with different motor types
   - Validate across different operating conditions
   - Compare performance with the research paper baseline

## Resources

- [Edge Impulse Documentation](https://docs.edgeimpulse.com/)
- [ESP32 Arduino Documentation](https://docs.espressif.com/projects/arduino-esp32/)
- [Original Research Paper](https://www.mdpi.com/1424-8220/21/22/7587)
