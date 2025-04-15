"""
EMD Preprocessing for Rotating Machine Fault Detection
-----------------------------------------------------
This script implements Empirical Mode Decomposition (EMD) preprocessing
for vibration signals as described in the research paper.

According to the paper:
1. The first IMF contains noise and is rejected
2. The remaining 9 IMFs and residual signal are combined
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PyEMD import EMD
from tqdm import tqdm

# Configuration
HEALTHY_DIR = '../dataset/processed/healthy/'
FAULTY_DIR = '../dataset/processed/faulty/'
OUTPUT_DIR = '../dataset/processed/emd_processed/'

# Create output directory if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(os.path.join(OUTPUT_DIR, 'healthy'), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_DIR, 'faulty'), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_DIR, 'plots'), exist_ok=True)

def apply_emd(signal, max_imfs=10):
    """Apply EMD to decompose the signal into IMFs"""
    emd = EMD()
    imfs = emd.emd(signal, max_imf=max_imfs)
    return imfs

def preprocess_signal(imfs):
    """Preprocess signal by rejecting first IMF and combining remaining IMFs"""
    # Skip first IMF (contains noise)
    processed_signal = np.sum(imfs[1:], axis=0)
    return processed_signal

def process_file(file_path, output_path, is_sample=False):
    """Process a single file using EMD"""
    # Load data
    data = pd.read_csv(file_path)
    
    # Process each axis
    processed_data = pd.DataFrame()
    
    # Initialize with timestamp and label columns
    processed_data['timestamp'] = data['timestamp']
    processed_data['label'] = data['label']
    
    # Process each axis
    for i in range(3):  # X, Y, Z axes
        signal = data.iloc[:, i].values
        
        # Apply EMD
        imfs = apply_emd(signal)
        
        # If this is a sample file, plot the IMFs
        if is_sample:
            plot_imfs(imfs, file_path, i)
        
        # Preprocess signal
        processed_signal = preprocess_signal(imfs)
        
        # Add to DataFrame
        processed_data[str(i)] = processed_signal
    
    # Save processed data
    processed_data.to_csv(output_path, index=False)
    return processed_data

def plot_imfs(imfs, file_path, axis_idx):
    """Plot IMFs for visualization"""
    filename = os.path.basename(file_path)
    class_name = 'healthy' if 'healthy' in file_path else 'faulty'
    axis_name = ['X', 'Y', 'Z'][axis_idx]
    
    n_imfs = len(imfs)
    plt.figure(figsize=(12, 2 * n_imfs))
    
    for i, imf in enumerate(imfs):
        plt.subplot(n_imfs, 1, i+1)
        plt.plot(imf)
        plt.title(f'IMF {i+1}')
        if i == 0:
            plt.title(f'IMF 1 (Noise - Rejected)')
        plt.ylabel('Amplitude')
        if i == n_imfs - 1:
            plt.xlabel('Sample')
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'plots', f'{class_name}_{axis_name}_{filename}_imfs.png'), dpi=300)
    plt.close()

def process_dataset():
    """Process the entire dataset"""
    # Process sample files first for visualization
    print("Processing sample files for visualization...")
    sample_healthy = os.path.join(HEALTHY_DIR, 'H1.csv')
    sample_faulty = os.path.join(FAULTY_DIR, 'F1.csv')
    
    process_file(sample_healthy, 
                os.path.join(OUTPUT_DIR, 'healthy', 'H1_processed.csv'), 
                is_sample=True)
    
    process_file(sample_faulty, 
                os.path.join(OUTPUT_DIR, 'faulty', 'F1_processed.csv'), 
                is_sample=True)
    
    # Process remaining healthy files
    print("Processing healthy files...")
    for file in tqdm(os.listdir(HEALTHY_DIR)):
        if file.endswith('.csv') and file != 'H1.csv':  # Skip the already processed sample
            input_path = os.path.join(HEALTHY_DIR, file)
            output_path = os.path.join(OUTPUT_DIR, 'healthy', f'{os.path.splitext(file)[0]}_processed.csv')
            process_file(input_path, output_path)
    
    # Process remaining faulty files
    print("Processing faulty files...")
    for file in tqdm(os.listdir(FAULTY_DIR)):
        if file.endswith('.csv') and file != 'F1.csv':  # Skip the already processed sample
            input_path = os.path.join(FAULTY_DIR, file)
            output_path = os.path.join(OUTPUT_DIR, 'faulty', f'{os.path.splitext(file)[0]}_processed.csv')
            process_file(input_path, output_path)

def compare_raw_vs_processed():
    """Compare raw signals with EMD-processed signals"""
    # Load sample data
    raw_healthy = pd.read_csv(os.path.join(HEALTHY_DIR, 'H1.csv'))
    raw_faulty = pd.read_csv(os.path.join(FAULTY_DIR, 'F1.csv'))
    
    processed_healthy = pd.read_csv(os.path.join(OUTPUT_DIR, 'healthy', 'H1_processed.csv'))
    processed_faulty = pd.read_csv(os.path.join(OUTPUT_DIR, 'faulty', 'F1_processed.csv'))
    
    # Plot comparison
    fig, axes = plt.subplots(2, 2, figsize=(16, 10))
    
    # Healthy raw
    axes[0, 0].plot(raw_healthy.iloc[:1000, 0], label='X')
    axes[0, 0].plot(raw_healthy.iloc[:1000, 1], label='Y')
    axes[0, 0].plot(raw_healthy.iloc[:1000, 2], label='Z')
    axes[0, 0].set_title('Raw Healthy Signal')
    axes[0, 0].set_xlabel('Sample')
    axes[0, 0].set_ylabel('Amplitude')
    axes[0, 0].legend()
    
    # Healthy processed
    axes[0, 1].plot(processed_healthy.iloc[:1000, 0], label='X')
    axes[0, 1].plot(processed_healthy.iloc[:1000, 1], label='Y')
    axes[0, 1].plot(processed_healthy.iloc[:1000, 2], label='Z')
    axes[0, 1].set_title('EMD-Processed Healthy Signal')
    axes[0, 1].set_xlabel('Sample')
    axes[0, 1].set_ylabel('Amplitude')
    axes[0, 1].legend()
    
    # Faulty raw
    axes[1, 0].plot(raw_faulty.iloc[:1000, 0], label='X')
    axes[1, 0].plot(raw_faulty.iloc[:1000, 1], label='Y')
    axes[1, 0].plot(raw_faulty.iloc[:1000, 2], label='Z')
    axes[1, 0].set_title('Raw Faulty Signal')
    axes[1, 0].set_xlabel('Sample')
    axes[1, 0].set_ylabel('Amplitude')
    axes[1, 0].legend()
    
    # Faulty processed
    axes[1, 1].plot(processed_faulty.iloc[:1000, 0], label='X')
    axes[1, 1].plot(processed_faulty.iloc[:1000, 1], label='Y')
    axes[1, 1].plot(processed_faulty.iloc[:1000, 2], label='Z')
    axes[1, 1].set_title('EMD-Processed Faulty Signal')
    axes[1, 1].set_xlabel('Sample')
    axes[1, 1].set_ylabel('Amplitude')
    axes[1, 1].legend()
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'plots', 'raw_vs_processed_comparison.png'), dpi=300)
    plt.close()

def main():
    print("Starting EMD preprocessing...")
    
    # Install PyEMD if not already installed
    try:
        import PyEMD
    except ImportError:
        print("PyEMD not found. Installing...")
        import subprocess
        subprocess.check_call(["pip", "install", "EMD-signal"])
    
    # Process the dataset
    process_dataset()
    
    # Compare raw vs processed
    compare_raw_vs_processed()
    
    print(f"EMD preprocessing complete! Processed files saved to {OUTPUT_DIR}")
    print("Note: This preprocessing step rejects the first IMF (containing noise) as per the research paper.")

if __name__ == "__main__":
    main() 