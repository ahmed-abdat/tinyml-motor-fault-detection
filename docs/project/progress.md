# Real-Time Vibration-Based Fault Detection for Rotating Machinery Using TinyML - Project Progress

## Project Overview

- **Title**: Real-Time Vibration-Based Fault Detection for Rotating Machinery Using TinyML
- **Student**: Ahmed Abdellahi Abdat
- **Institution**: Faculty of Sciences of Bizerte
- **Program**: Master's in Electronics, Electrical Engineering and Automation
- **Start Date**: April 2025
- **Target Completion**: September 2025

## Dataset Information

- **Source**: Vibration Faults Dataset for Rotating Machines (Kaggle)
- **Citation**: M. U. Khan, M. A. Imtiaz, S. Aziz, Z. Kareem, A. Waseem and M. A. Akram, "System Design for Early Fault Diagnosis of Machines using Vibration Features," 2019 International Conference on Power Generation Systems and Renewable Energy Technologies (PGSRET)
- **Content**:
  - Normal samples: 103 signals (5 seconds each @ 1000Hz)
  - Faulty samples: 117 signals (5 seconds each @ 1000Hz)
  - Data format: Converted from .mat to CSV (X, Y, Z axes values)

## Project Timeline and Progress Tracking

### Phase 1: Dataset Preparation and Understanding

**Status**: Completed ✅

- [x] Convert dataset to appropriate format
- [x] Analyze signal characteristics
- [x] Visualize samples from all states
- [x] Calculate statistics for each state
- [x] Evaluate and document distinguishing features

### Phase 2: Edge Impulse Project Setup

**Status**: Completed ✅

- [x] Create new Edge Impulse project
- [x] Configure project parameters
- [x] Upload dataset to Edge Impulse
- [x] Split data into training/testing sets
- [x] Verify data integrity in Edge Impulse

### Phase 3: Feature Extraction Implementation

**Status**: Completed ✅

- [x] Configure processing blocks in Edge Impulse
- [x] Implement time domain features
  - [x] Mean, Standard Deviation, RMS
  - [x] Skewness, Kurtosis
  - [x] Peak to Peak, Energy
- [x] Implement frequency domain features
  - [x] Mean Frequency, Frequency Std Dev
  - [x] Spectral Centroid, Spectral Flux
  - [x] Spectral Roll-off, Flatness, Crest
  - [x] Spectral Decrease, Slope, Spread
- [x] Evaluate feature performance
- [x] Select optimal feature combination

### Phase 4: Model Training and Optimization

**Status**: Completed ✅

- [x] Train neural network model
- [x] Optimize architecture (96-32 neurons with dropout)
- [x] Apply quantization techniques (int8)
- [x] Reduce model size for ESP32 deployment
- [x] Exceeded target accuracy (achieved 100% on test set!)

Performance Metrics:

- Training accuracy: 97.2%
- Test accuracy: 100%
- Inference time: 4ms
- Peak RAM usage: 2.7KB
- Flash usage: 137.3KB

### Phase 5: ESP32 Deployment

**Status**: Ready to Start ⏳

- [ ] Export optimized model from Edge Impulse
- [ ] Set up ESP32 development environment
- [ ] Develop firmware for data acquisition
- [ ] Implement preprocessing on ESP32
- [ ] Integrate inference engine
- [ ] Connect accelerometer hardware
- [ ] Test real-time performance
- [ ] Optimize for power efficiency

### Phase 6: Validation and Documentation

**Status**: Not Started ❌

- [ ] Validate system with new test data
- [ ] Measure and document performance metrics
- [ ] Write technical documentation
- [ ] Prepare final report
- [ ] Create presentation slides

## Current Focus

- Preparing for ESP32 deployment
- Planning hardware integration
- Setting up development environment for ESP32

## Challenges & Solutions

| Date         | Challenge                               | Solution                                                                                     | Status      |
| ------------ | --------------------------------------- | -------------------------------------------------------------------------------------------- | ----------- |
| Current week | Initial plan included EMD preprocessing | Determined EMD preprocessing unnecessary as Edge Impulse provides built-in signal processing | Resolved ✅ |

## Weekly Updates

### Week 1 (Completed)

- Acquired dataset from Kaggle
- Created project structure
- Set up GitHub repository
- Implemented visualization and analysis
- Generated high-quality signal visualizations for documentation

### Week 2 (Completed)

- Completed Edge Impulse project setup
- Successfully implemented feature extraction
- Achieved excellent model performance
- Optimized model for ESP32 deployment

### Week 3 (Current)

- Achieved 100% accuracy on test dataset
- Successfully quantized model to int8
- Verified model performance metrics
- Ready for ESP32 deployment phase

### Next Steps

- Export optimized model from Edge Impulse
- Set up ESP32 development environment
- Begin hardware integration planning
