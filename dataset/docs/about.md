# About Dataset

This dataset contains vibrational data collected for the purpose of diagnosing faults in large industrial induction motors. The data was used in the research work titled "An Expert System for Rotating Machine Fault Detection Using Vibration Signal Analysis" published in Sensors.

In order to use this dataset, please cite this article:
> Kafeel A, Aziz S, Awais M, Khan MA, Afaq K, Idris SA, Alshazly H, Mostafa SM. An Expert System for Rotating Machine Fault Detection Using Vibration Signal Analysis. Sensors. 2021; 21(22):7587. https://doi.org/10.3390/s21227587.

## Data Collection

- **Sensor Used**: Beanscape tri-axis wireless accelerometer
- **Sampling Rate**: 1000 Hz for each of the three axes (X, Y, and Z)
- **Experiment Location**: Large industrial enterprise
- **Working States**: The dataset includes two working states of the machinery:
  - Normal state
  - Faulty state - (including bearing and alignment faults)

## Experimental Setup

The experimental setup involves the following components and procedures:

- **Equipment**: 45 KW three-phase induction motors coupled with centrifugal water pumps
- **Sensor Mounting**: The accelerometer was mounted at various positions on both faulty and normally running motors
- **Signal Acquisition**: The accelerometer captures individual signals for vibrations along the X, Y, and Z axes, which are then combined into a single time domain composite signal

## Dataset Structure

### Data Classes

- **Normal**: 103 signals, each with a duration of 5 seconds (totaling 8.5 minutes)
- **Faulty**: 117 signals, each with a duration of 5 seconds (totaling 9.75 minutes)
- **Total**: 220 signals, with a combined duration of 18.25 minutes
- **File Type**: The dataset files are in MATLAB format (.mat)
- **Software Used**: MATLAB was utilized for signal processing and analysis

## Usage Notes

The dataset is provided as-is for research and educational purposes. Please cite the associated paper when using this dataset. For further details on the dataset and experimental setup, refer to the following article:

> Kafeel A, Aziz S, Awais M, Khan MA, Afaq K, Idris SA, Alshazly H, Mostafa SM. An Expert System for Rotating Machine Fault Detection Using Vibration Signal Analysis. Sensors. 2021; 21(22):7587. https://doi.org/10.3390/s21227587.

For a comparative study or reference to previous similar datasets, you may consider the dataset used in the research titled "System Design for Early Fault Diagnosis of Machines using Vibration Features," published at the 2019 International Conference on Power Generation Systems and Renewable Energy Technologies (PGSRET). This dataset can be accessed at:

https://www.kaggle.com/datasets/sumairaziz/vibration-based-fault-diagnosis-of-machines