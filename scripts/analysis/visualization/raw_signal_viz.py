"""
Functions for visualizing raw vibration signals from the dataset.
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import pandas as pd
import os

# Constants and configuration parameters
FIGURE_SIZE = (12, 6)
COLORS = {
    'normal': '#2ecc71',  # Green
    'faulty': '#e74c3c',  # Red
    'grid': '#95a5a6',    # Gray
}
LABELS = {
    'time': 'Time (s)',
    'amplitude': 'Amplitude (g)',
    'normal': 'Normal State',
    'faulty': 'Faulty State'
}
SAMPLING_RATE = 1000  # Hz
SIGNAL_DURATION = 5   # seconds

# Output directory for saved figures
OUTPUT_DIR = "visualization_results"

def ensure_output_dir():
    """Create output directory if it doesn't exist"""
    # Get the root directory (3 levels up from this script)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.abspath(os.path.join(script_dir, '..', '..', '..'))
    output_path = os.path.join(root_dir, OUTPUT_DIR)
    
    if not os.path.exists(output_path):
        os.makedirs(output_path)
        print(f"Created output directory: {output_path}")
    
    return output_path

def generate_time_axis(n_samples):
    """Generate time axis based on sampling rate"""
    return np.linspace(0, SIGNAL_DURATION, n_samples)

def combine_xyz_signals(x, y, z):
    """Combine X, Y, Z acceleration signals into a composite signal"""
    return np.sqrt(x**2 + y**2 + z**2)

def normalize_signal(signal):
    """Normalize signal by dividing by maximum amplitude"""
    max_amp = np.max(np.abs(signal))
    return signal / max_amp if max_amp != 0 else signal

def plot_xyz_signals(data, title="Raw XYZ Signals", save=True, show=True):
    """
    Plot X, Y, Z acceleration signals.
    
    Args:
        data: DataFrame containing columns 0, 1, 2 for X, Y, Z
        title: Plot title
        save: Whether to save the plot as an image file
        show: Whether to display the plot
    
    Returns:
        Path to saved image file if save=True, None otherwise
    """
    time = generate_time_axis(len(data))
    
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=FIGURE_SIZE, sharex=True)
    fig.suptitle(title)
    
    # Plot X-axis
    ax1.plot(time, data['0'], color=COLORS['normal'])
    ax1.set_ylabel('X-axis (g)')
    ax1.grid(True, color=COLORS['grid'], alpha=0.3)
    
    # Plot Y-axis
    ax2.plot(time, data['1'], color=COLORS['normal'])
    ax2.set_ylabel('Y-axis (g)')
    ax2.grid(True, color=COLORS['grid'], alpha=0.3)
    
    # Plot Z-axis
    ax3.plot(time, data['2'], color=COLORS['normal'])
    ax3.set_xlabel(LABELS['time'])
    ax3.set_ylabel('Z-axis (g)')
    ax3.grid(True, color=COLORS['grid'], alpha=0.3)
    
    plt.tight_layout()
    
    saved_path = None
    if save:
        output_dir = ensure_output_dir()
        filename = f"{title.replace(' ', '_').lower()}.png"
        saved_path = os.path.join(output_dir, filename)
        plt.savefig(saved_path, dpi=300)
        print(f"Saved figure to {saved_path}")
    
    if show:
        plt.show()
    else:
        plt.close()
    
    return saved_path

def plot_combined_signal(data, title="Combined Signal", save=True, show=True):
    """
    Plot combined XYZ signal.
    
    Args:
        data: DataFrame containing columns 0, 1, 2 for X, Y, Z
        title: Plot title
        save: Whether to save the plot as an image file
        show: Whether to display the plot
    
    Returns:
        Path to saved image file if save=True, None otherwise
    """
    time = generate_time_axis(len(data))
    combined = combine_xyz_signals(
        data['0'].values,
        data['1'].values,
        data['2'].values
    )
    combined_norm = normalize_signal(combined)
    
    plt.figure(figsize=FIGURE_SIZE)
    plt.plot(time, combined_norm, color=COLORS['normal'])
    plt.title(title)
    plt.xlabel(LABELS['time'])
    plt.ylabel(LABELS['amplitude'])
    plt.grid(True, color=COLORS['grid'], alpha=0.3)
    plt.tight_layout()
    
    saved_path = None
    if save:
        output_dir = ensure_output_dir()
        filename = f"{title.replace(' ', '_').lower()}.png"
        saved_path = os.path.join(output_dir, filename)
        plt.savefig(saved_path, dpi=300)
        print(f"Saved figure to {saved_path}")
    
    if show:
        plt.show()
    else:
        plt.close()
    
    return saved_path

def compare_normal_faulty(normal_data, faulty_data, title="Normal vs Faulty Signal Comparison", save=True, show=True):
    """
    Compare normal and faulty signals.
    
    Args:
        normal_data: DataFrame containing normal state signals
        faulty_data: DataFrame containing faulty state signals
        title: Plot title
        save: Whether to save the plot as an image file
        show: Whether to display the plot
    
    Returns:
        Path to saved image file if save=True, None otherwise
    """
    time = generate_time_axis(len(normal_data))
    
    # Process normal signal
    normal_combined = combine_xyz_signals(
        normal_data['0'].values,
        normal_data['1'].values,
        normal_data['2'].values
    )
    normal_norm = normalize_signal(normal_combined)
    
    # Process faulty signal
    faulty_combined = combine_xyz_signals(
        faulty_data['0'].values,
        faulty_data['1'].values,
        faulty_data['2'].values
    )
    faulty_norm = normalize_signal(faulty_combined)
    
    # Create comparison plot
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=FIGURE_SIZE, sharex=True)
    fig.suptitle(title)
    
    # Plot normal signal
    ax1.plot(time, normal_norm, color=COLORS['normal'], label=LABELS['normal'])
    ax1.set_ylabel(LABELS['amplitude'])
    ax1.grid(True, color=COLORS['grid'], alpha=0.3)
    ax1.legend()
    
    # Plot faulty signal
    ax2.plot(time, faulty_norm, color=COLORS['faulty'], label=LABELS['faulty'])
    ax2.set_xlabel(LABELS['time'])
    ax2.set_ylabel(LABELS['amplitude'])
    ax2.grid(True, color=COLORS['grid'], alpha=0.3)
    ax2.legend()
    
    plt.tight_layout()
    
    saved_path = None
    if save:
        output_dir = ensure_output_dir()
        filename = f"{title.replace(' ', '_').lower()}.png"
        saved_path = os.path.join(output_dir, filename)
        plt.savefig(saved_path, dpi=300)
        print(f"Saved figure to {saved_path}")
    
    if show:
        plt.show()
    else:
        plt.close()
    
    return saved_path

if __name__ == "__main__":
    # Example usage with our actual dataset structure
    print("Loading and visualizing sample data...")
    
    # Get the root directory (3 levels up from this script)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.abspath(os.path.join(script_dir, '..', '..', '..'))
    
    # Define the paths to the data files
    healthy_file = os.path.join(root_dir, "dataset", "processed", "healthy", "H1.csv")
    faulty_file = os.path.join(root_dir, "dataset", "processed", "faulty", "F1.csv")
    
    print(f"Looking for files at:\n{healthy_file}\n{faulty_file}")
    
    # Check if files exist
    if not os.path.exists(healthy_file) or not os.path.exists(faulty_file):
        print(f"Error: Required data files not found")
    else:
        # Load the data
        healthy_data = pd.read_csv(healthy_file)
        faulty_data = pd.read_csv(faulty_file)
        
        # Set default behavior for plots (save=True, show=True)
        save_plots = True
        show_plots = True
        
        # Create output directory
        if save_plots:
            output_dir = ensure_output_dir()
            print(f"Visualizations will be saved to: {output_dir}")
        
        # Visualize individual signals
        print("1. Visualizing healthy state signal...")
        plot_xyz_signals(healthy_data, title="Healthy State - Raw XYZ Signals", 
                         save=save_plots, show=show_plots)
        
        print("2. Visualizing faulty state signal...")
        plot_xyz_signals(faulty_data, title="Faulty State - Raw XYZ Signals", 
                         save=save_plots, show=show_plots)
        
        # Visualize combined signals
        print("3. Visualizing combined healthy signal...")
        plot_combined_signal(healthy_data, title="Healthy State - Combined Signal", 
                             save=save_plots, show=show_plots)
        
        print("4. Visualizing combined faulty signal...")
        plot_combined_signal(faulty_data, title="Faulty State - Combined Signal", 
                             save=save_plots, show=show_plots)
        
        # Compare signals
        print("5. Comparing healthy and faulty signals...")
        compare_normal_faulty(healthy_data, faulty_data, 
                              save=save_plots, show=show_plots)
        
        if save_plots:
            print(f"\nAll visualizations have been saved to: {output_dir}") 