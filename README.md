# TinyML Rotating Machine Fault Detection

> Master's thesis project in Electronics, Electrical Engineering and Automation at Faculty of Sciences of Bizerte

## Project Overview

ESP32-based fault detection system for rotating machines using vibration analysis and TinyML. The system uses Edge Impulse for model development and deploys on ESP32 for real-time fault detection.

### Key Features

- Real-time vibration analysis using tri-axial accelerometer
- TinyML model for fault detection with 95%+ accuracy
- ESP32-based embedded deployment
- Comprehensive signal processing pipeline
- Edge Impulse integration

## Project Structure

```
.
├── docs/               # Documentation and research papers
├── dataset/           # Vibration signal dataset and metadata
├── edge_impulse/      # Edge Impulse model development
├── esp32/             # ESP32 firmware and deployment code
├── scripts/           # Data processing and analysis scripts
└── requirements.txt   # Python dependencies
```

## Dataset

This project uses the ["Vibration Faults Dataset for Rotating Machines"](https://www.kaggle.com/datasets/sumairaziz/vibration-faults-dataset-for-rotating-machines) from Kaggle. The dataset includes:

- **Sensor Used**: SG-Link tri-axial accelerometer sensor by MICROSTRAIN Corporation
- **Sampling Rate**: 679 samples per second for each axis
- **Working States**:
  - Normal state
  - Cracking state
  - Offset pulley state
  - Wear state
- **Data Collection**: Conducted at Mechanical Vibration Laboratory, MED, UET Taxila

Please cite the following paper when using this dataset:

> M. U. Khan, M. A. Imtiaz, S. Aziz, Z. Kareem, A. Waseem and M. A. Akram, "System Design for Early Fault Diagnosis of Machines using Vibration Features," 2019 International Conference on Power Generation Systems and Renewable Energy Technologies (PGSRET)

## Getting Started

### Prerequisites

- Python 3.8+
- ESP32 development board
- Edge Impulse account
- Tri-axial accelerometer

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

## Development Progress

Track the development progress in [Project Progress](docs/project/progress.md)

## Documentation (Coming Soon)

The following documentation is under development and will be added progressively:

- Setup Instructions
- Hardware Configuration Guide
- Signal Processing Pipeline Documentation
- Model Development Guide
- ESP32 Deployment Instructions
- Performance Metrics Report

## Author

**Ahmed Abdellahi Abdat**  
Master's Student  
Faculty of Sciences of Bizerte  
Electronics, Electrical Engineering and Automation

## Academic Context

This repository contains the implementation work for my Master's thesis project (PFE) focused on fault characterization in rotating motors using TinyML.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Faculty of Sciences of Bizerte
- Project Supervisor: [Dr. Khalil Jouili](https://www.researchgate.net/profile/Khalil-Jouili) - Faculty of Sciences of Bizerte
- Dataset Authors: M. U. Khan, M. A. Imtiaz, S. Aziz, et al.
- Dataset source: [Vibration Faults Dataset for Rotating Machines (Kaggle)](https://www.kaggle.com/datasets/sumairaziz/vibration-faults-dataset-for-rotating-machines)
