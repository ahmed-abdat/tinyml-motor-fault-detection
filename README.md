# Real-Time Vibration-Based Fault Detection for Rotating Machinery Using TinyML

> Master's project (PFE) in Electronics, Electrical Engineering and Automation at Faculty of Sciences of Bizerte

## Project Overview

ESP32-based fault detection system for rotating machines using vibration analysis and TinyML. The system uses Edge Impulse for model development and deploys on ESP32 for real-time fault detection.

### Performance Metrics ✨

- 100% test accuracy, 97.2% training accuracy
- 4ms inference time
- 2.7KB RAM usage, 137.3KB Flash usage
- Optimized for ESP32 deployment

### Key Features

- Real-time vibration analysis using tri-axial accelerometer
- Optimized TinyML model with perfect classification
- Spectral analysis with advanced feature extraction
- Comprehensive signal processing pipeline
- Edge Impulse integration with quantization

## Project Structure

```
.
├── docs/               # Documentation and research papers
├── dataset/           # Vibration signal dataset (220 samples)
├── edge_impulse/      # Edge Impulse model development
├── esp32/             # ESP32 firmware and deployment code
├── scripts/           # Data processing and analysis scripts
└── requirements.txt   # Python dependencies
```

## Implementation Status

✅ Dataset Preparation & Analysis
✅ Edge Impulse Project Setup
✅ Feature Extraction Implementation
✅ Model Training & Optimization
⏳ ESP32 Deployment
❌ Final Validation & Documentation

For detailed progress, see [Project Progress](docs/project/progress.md)

## Getting Started

### Prerequisites

- Python 3.8+
- ESP32 development board
- Edge Impulse account
- Tri-axial accelerometer (1000Hz sampling)

### Installation

1. Clone the repository

```bash
git clone https://github.com/ahmed-abdat/tinyml-motor-fault-detection.git
cd tinyml-motor-fault-detection
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

## Documentation

- [Edge Impulse Guide](docs/edge_impulse/README.md) - Complete implementation guide
- [Project Progress](docs/project/progress.md) - Detailed progress tracking
- [Dataset Info](dataset/docs/about.md) - Dataset documentation

Coming Soon:

- ESP32 Deployment Guide
- Hardware Configuration Guide
- Performance Analysis Report

## Author

**Ahmed Abdellahi Abdat**  
Master's Student  
Faculty of Sciences of Bizerte  
Electronics, Electrical Engineering and Automation

## Academic Context

This repository contains the implementation work for my Master's thesis project (PFE) focused on real-time fault detection in rotating machinery using TinyML and vibration analysis.

## Acknowledgments

- Faculty of Sciences of Bizerte
- Project Supervisor: [Dr. Khalil Jouili](https://www.researchgate.net/profile/Khalil-Jouili)
- Dataset Authors: M. U. Khan, M. A. Imtiaz, S. Aziz, et al.
- Dataset: [Vibration Faults Dataset (Kaggle)](https://www.kaggle.com/datasets/sumairaziz/vibration-faults-dataset-for-rotating-machines)
