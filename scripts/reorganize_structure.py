"""
Reorganize Project Structure Script
---------------------------------
This script reorganizes the current project structure into a standardized format
for the rotating machine fault detection project.
"""

import os
import shutil
from pathlib import Path

def create_directory_structure(base_path):
    """Create the new directory structure."""
    # Define the directory structure
    directories = [
        'dataset/raw/healthy',
        'dataset/raw/faulty',
        'dataset/processed/healthy',
        'dataset/processed/faulty',
        'dataset/docs/paper',
        'docs/project',
        'docs/technical',
        'docs/references',
        'scripts/analysis',
        'scripts/deployment',
        'edge_impulse/data',
        'edge_impulse/models',
        'esp32/src',
        'esp32/lib'
    ]
    
    # Create directories
    for dir_path in directories:
        full_path = os.path.join(base_path, dir_path)
        os.makedirs(full_path, exist_ok=True)
        print(f"Created directory: {full_path}")

def move_existing_files(base_path):
    """Move existing files to their new locations."""
    # Move raw dataset files
    if os.path.exists('Healthy'):
        print("Moving raw Healthy data...")
        healthy_files = os.listdir('Healthy')
        for file in healthy_files:
            src = os.path.join('Healthy', file)
            dst = os.path.join(base_path, 'dataset/raw/healthy', file)
            shutil.move(src, dst)
            print(f"Moved {src} to {dst}")
        os.rmdir('Healthy')  # Remove empty directory
        
    if os.path.exists('Faulty'):
        print("Moving raw Faulty data...")
        faulty_files = os.listdir('Faulty')
        for file in faulty_files:
            src = os.path.join('Faulty', file)
            dst = os.path.join(base_path, 'dataset/raw/faulty', file)
            shutil.move(src, dst)
            print(f"Moved {src} to {dst}")
        os.rmdir('Faulty')  # Remove empty directory
    
    # Move processed dataset files
    if os.path.exists('dataset_csv/healthy'):
        shutil.move('dataset_csv/healthy', os.path.join(base_path, 'dataset/processed/healthy'))
    if os.path.exists('dataset_csv/faulty'):
        shutil.move('dataset_csv/faulty', os.path.join(base_path, 'dataset/processed/faulty'))
    
    # Move project tracking files
    if os.path.exists('project_tracking/project_progress.md'):
        shutil.move('project_tracking/project_progress.md', 
                   os.path.join(base_path, 'docs/project/progress.md'))
    
    if os.path.exists('project_tracking/edge_impulse_setup.md'):
        shutil.move('project_tracking/edge_impulse_setup.md', 
                   os.path.join(base_path, 'docs/technical/edge_impulse.md'))
    
    if os.path.exists('project_tracking/data_analysis.py'):
        shutil.move('project_tracking/data_analysis.py', 
                   os.path.join(base_path, 'scripts/analysis/visualize.py'))

def create_placeholder_files(base_path):
    """Create placeholder files with basic content."""
    files = {
        'README.md': """# Rotating Machine Fault Detection using TinyML

This project implements fault detection for rotating machines using TinyML and Edge Impulse.
The system is deployed on an ESP32 microcontroller for real-time monitoring.

## Project Structure
[Directory structure description]

## Setup Instructions
[Setup steps]

## Usage
[Usage instructions]

## License
[License information]
""",
        'dataset/docs/about.md': """# Dataset Description

This dataset contains vibration measurements from rotating machines in both healthy and faulty states.
The data was collected using a three-axis accelerometer at 1000Hz sampling rate.

## Data Format
- Healthy samples: 103 signals (5 seconds each @ 1000Hz)
- Faulty samples: 117 signals (5 seconds each @ 1000Hz)
""",
        'docs/project/context.md': """# Project Context

## Background
This project aims to implement fault detection in rotating machines using TinyML approach.
The system will be deployed on an ESP32 microcontroller for real-time monitoring.

## Requirements
[Project requirements]
""",
        'esp32/hardware.md': """# Hardware Setup Guide

## Components Required
- ESP32 Development Board
- MPU6050 Accelerometer
- Connecting wires
- USB cable

## Connections
[Connection diagram and instructions]
""",
        'edge_impulse/settings.md': """# Edge Impulse Project Settings

## Project Configuration
- Sample frequency (Hz): 1000
- Sample length (ms): 5000
- Sensor axes: 3 (X, Y, Z)

## Processing Blocks
[Processing block configuration]
"""
    }
    
    for file_path, content in files.items():
        full_path = os.path.join(base_path, file_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Created file: {full_path}")

def main():
    """Main function to reorganize the project structure."""
    base_path = '.'
    
    print("Starting project reorganization...")
    
    # Create new directory structure
    create_directory_structure(base_path)
    
    # Move existing files
    move_existing_files(base_path)
    
    # Create placeholder files
    create_placeholder_files(base_path)
    
    print("\nProject reorganization complete!")
    print("Please review the new structure and update any file paths in your code accordingly.")

if __name__ == "__main__":
    main() 