"""
Data Analysis for Rotating Machine Fault Detection
--------------------------------------------------
This script analyzes the vibration dataset for fault detection in rotating machines.
It generates visualizations and statistical analysis to better understand the dataset.
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
from scipy.stats import skew, kurtosis
import seaborn as sns
from tqdm import tqdm

# Configuration
HEALTHY_DIR = '../dataset_csv/healthy/'
FAULTY_DIR = '../dataset_csv/faulty/'
OUTPUT_DIR = 'analysis_results/'

# Create output directory if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

def load_sample_data(healthy_file, faulty_file):
    """Load sample data from one healthy and one faulty file"""
    healthy = pd.read_csv(os.path.join(HEALTHY_DIR, healthy_file))
    faulty = pd.read_csv(os.path.join(FAULTY_DIR, faulty_file))
    return healthy, faulty

def plot_time_series(healthy, faulty, n_samples=1000):
    """Plot time series data for both healthy and faulty signals"""
    fig, axes = plt.subplots(2, 3, figsize=(18, 10))
    
    # Plot each axis separately
    for i, axis_name in enumerate(['X-axis (0)', 'Y-axis (1)', 'Z-axis (2)']):
        # Healthy data
        axes[0, i].plot(healthy.iloc[:n_samples, i])
        axes[0, i].set_title(f'Healthy Motor - {axis_name}')
        axes[0, i].set_xlabel('Sample')
        axes[0, i].set_ylabel('Amplitude')
        
        # Faulty data
        axes[1, i].plot(faulty.iloc[:n_samples, i])
        axes[1, i].set_title(f'Faulty Motor - {axis_name}')
        axes[1, i].set_xlabel('Sample')
        axes[1, i].set_ylabel('Amplitude')
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'time_series_comparison.png'), dpi=300)
    
def plot_3d_signals(healthy, faulty, n_samples=1000):
    """Plot 3D visualization of signals"""
    fig = plt.figure(figsize=(18, 8))
    
    # Healthy signal
    ax1 = fig.add_subplot(121, projection='3d')
    ax1.plot(healthy.iloc[:n_samples, 0], 
             healthy.iloc[:n_samples, 1], 
             healthy.iloc[:n_samples, 2])
    ax1.set_title('Healthy Motor 3D Vibration')
    ax1.set_xlabel('X-axis')
    ax1.set_ylabel('Y-axis')
    ax1.set_zlabel('Z-axis')
    
    # Faulty signal
    ax2 = fig.add_subplot(122, projection='3d')
    ax2.plot(faulty.iloc[:n_samples, 0], 
             faulty.iloc[:n_samples, 1], 
             faulty.iloc[:n_samples, 2])
    ax2.set_title('Faulty Motor 3D Vibration')
    ax2.set_xlabel('X-axis')
    ax2.set_ylabel('Y-axis')
    ax2.set_zlabel('Z-axis')
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, '3d_signal_comparison.png'), dpi=300)

def plot_fft_spectrum(healthy, faulty, n_samples=5000, fs=1000):
    """Plot FFT spectrum for both signals"""
    fig, axes = plt.subplots(2, 3, figsize=(18, 10))
    
    # Frequency range
    freq = np.fft.fftfreq(n_samples, d=1/fs)
    freq = freq[:n_samples//2]
    
    # Plot each axis separately
    for i, axis_name in enumerate(['X-axis (0)', 'Y-axis (1)', 'Z-axis (2)']):
        # Healthy data
        fft_healthy = np.abs(fft(healthy.iloc[:n_samples, i]))
        fft_healthy = fft_healthy[:n_samples//2]
        axes[0, i].plot(freq, fft_healthy)
        axes[0, i].set_title(f'Healthy Motor FFT - {axis_name}')
        axes[0, i].set_xlabel('Frequency (Hz)')
        axes[0, i].set_ylabel('Magnitude')
        
        # Faulty data
        fft_faulty = np.abs(fft(faulty.iloc[:n_samples, i]))
        fft_faulty = fft_faulty[:n_samples//2]
        axes[1, i].plot(freq, fft_faulty)
        axes[1, i].set_title(f'Faulty Motor FFT - {axis_name}')
        axes[1, i].set_xlabel('Frequency (Hz)')
        axes[1, i].set_ylabel('Magnitude')
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'fft_spectrum_comparison.png'), dpi=300)

def extract_features(data):
    """Extract time and frequency domain features from signal data"""
    features = {}
    
    # Time domain features
    features['mean'] = np.mean(data)
    features['std'] = np.std(data)
    features['rms'] = np.sqrt(np.mean(np.square(data)))
    features['skewness'] = skew(data)
    features['kurtosis'] = kurtosis(data)
    features['peak_to_peak'] = np.max(data) - np.min(data)
    features['energy'] = np.sum(np.square(data))
    
    # Frequency domain features
    fft_data = np.abs(fft(data))
    fft_data = fft_data[:len(data)//2]
    freq = np.fft.fftfreq(len(data), d=1/1000)
    freq = freq[:len(data)//2]
    
    features['mean_freq'] = np.mean(fft_data)
    features['std_freq'] = np.std(fft_data)
    
    # Calculate spectral centroid
    if np.sum(fft_data) > 0:
        features['spectral_centroid'] = np.sum(freq * fft_data) / np.sum(fft_data)
    else:
        features['spectral_centroid'] = 0
    
    return features

def analyze_dataset_statistics():
    """Analyze statistics across the entire dataset"""
    # Create empty DataFrames to store results
    healthy_stats = pd.DataFrame()
    faulty_stats = pd.DataFrame()
    
    # Process healthy files
    print("Processing healthy files...")
    for file in tqdm(os.listdir(HEALTHY_DIR)):
        if file.endswith('.csv'):
            data = pd.read_csv(os.path.join(HEALTHY_DIR, file))
            
            # Extract features for each axis
            for i, axis in enumerate(['x', 'y', 'z']):
                features = extract_features(data.iloc[:, i])
                features['file'] = file
                features['axis'] = axis
                healthy_stats = pd.concat([healthy_stats, pd.DataFrame([features])])
    
    # Process faulty files
    print("Processing faulty files...")
    for file in tqdm(os.listdir(FAULTY_DIR)):
        if file.endswith('.csv'):
            data = pd.read_csv(os.path.join(FAULTY_DIR, file))
            
            # Extract features for each axis
            for i, axis in enumerate(['x', 'y', 'z']):
                features = extract_features(data.iloc[:, i])
                features['file'] = file
                features['axis'] = axis
                faulty_stats = pd.concat([faulty_stats, pd.DataFrame([features])])
    
    # Save statistics to CSV
    healthy_stats.to_csv(os.path.join(OUTPUT_DIR, 'healthy_statistics.csv'), index=False)
    faulty_stats.to_csv(os.path.join(OUTPUT_DIR, 'faulty_statistics.csv'), index=False)
    
    # Generate statistical comparison plots
    plot_feature_comparisons(healthy_stats, faulty_stats)
    
    return healthy_stats, faulty_stats

def plot_feature_comparisons(healthy_stats, faulty_stats):
    """Plot comparisons of key features between healthy and faulty data"""
    # Combine data for plotting
    healthy_stats['class'] = 'healthy'
    faulty_stats['class'] = 'faulty'
    all_stats = pd.concat([healthy_stats, faulty_stats])
    
    # Plot key features
    features_to_plot = ['mean', 'std', 'rms', 'skewness', 'kurtosis', 
                       'peak_to_peak', 'mean_freq', 'spectral_centroid']
    
    for feature in features_to_plot:
        plt.figure(figsize=(12, 6))
        sns.boxplot(x='axis', y=feature, hue='class', data=all_stats)
        plt.title(f'{feature.capitalize()} Comparison Between Healthy and Faulty States')
        plt.savefig(os.path.join(OUTPUT_DIR, f'{feature}_comparison.png'), dpi=300)
        plt.close()

def main():
    print("Starting data analysis...")
    
    # Load sample data for visualization
    print("Loading sample data...")
    healthy, faulty = load_sample_data('H1.csv', 'F1.csv')
    
    # Generate time series plots
    print("Generating time series plots...")
    plot_time_series(healthy, faulty)
    
    # Generate 3D signal plots
    print("Generating 3D signal plots...")
    plot_3d_signals(healthy, faulty)
    
    # Generate FFT spectrum plots
    print("Generating FFT spectrum plots...")
    plot_fft_spectrum(healthy, faulty)
    
    # Analyze dataset statistics
    print("Analyzing dataset statistics (this may take a while)...")
    healthy_stats, faulty_stats = analyze_dataset_statistics()
    
    print(f"Analysis complete! Results saved to {OUTPUT_DIR}")

if __name__ == "__main__":
    main() 