# Edge Impulse Implementation: Vibration-Based Fault Detection

## Performance Metrics

- 100% test accuracy, 97.2% training accuracy
- 4ms inference time
- 2.7KB RAM, 137.3KB Flash usage

## Quick Setup

1. Project Configuration

   - Name: "Rotating-Machine-Fault-Detection"
   - Type: Binary Classification (normal/faulty)
   - Sample length: 5000 samples @ 1000Hz
   - Dataset: 220 samples (103 normal, 117 faulty)

2. Signal Processing

   - Spectral Analysis block
   - Frame length: 0.1s, FFT length: 256
   - Frequency range: 0-200Hz
   - Window: Hanning

3. Neural Network

```python
model = Sequential([
    Dense(96, activation='relu'),
    Dropout(0.2),
    Dense(32, activation='relu'),
    Dropout(0.2),
    Dense(2, activation='softmax')
])
```

4. Training Settings
   - Adam optimizer (lr=0.001)
   - 100 epochs, batch size=32
   - Int8 quantization enabled

## ESP32 Implementation

```cpp
#include <EdgeImpulse_InferenceModel.h>

static float buffer[EI_CLASSIFIER_DSP_INPUT_FRAME_SIZE] = { 0 };

void setup() {
    Serial.begin(115200);
    // Initialize accelerometer
}

void loop() {
    // Read accelerometer data at 1000Hz
    for (size_t i = 0; i < EI_CLASSIFIER_DSP_INPUT_FRAME_SIZE; i += 3) {
        buffer[i + 0] = ax;  // X-axis
        buffer[i + 1] = ay;  // Y-axis
        buffer[i + 2] = az;  // Z-axis
        delay(1);
    }

    // Run inference
    ei_impulse_result_t result;
    run_classifier(buffer, EI_CLASSIFIER_DSP_INPUT_FRAME_SIZE, &result, true);

    // Print results
    for (size_t ix = 0; ix < EI_CLASSIFIER_LABEL_COUNT; ix++) {
        Serial.printf("%s: %.2f\n", result.classification[ix].label,
                                   result.classification[ix].value);
    }
    delay(1000);
}
```

## Troubleshooting

1. Low Accuracy

   - Increase training epochs
   - Adjust dropout rates
   - Verify data quality

2. Deployment Issues
   - Check memory usage
   - Verify sampling rate
   - Monitor serial output

## Resources

- [Edge Impulse Docs](https://docs.edgeimpulse.com)
- [ESP32 Docs](https://docs.espressif.com)
- [Project Repository](https://github.com/ahmed-abdat/tinyml-motor-fault-detection)
