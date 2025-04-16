"""
Example script demonstrating the use of visualization functions.
"""

from pathlib import Path
from raw_signal_viz import plot_xyz_signals, plot_combined_signal, compare_normal_faulty
from utils import load_signal_data

def main():
    # Paths to your data files (update these paths according to your data location)
    normal_file = Path("dataset/raw/normal/sample1.csv")
    faulty_file = Path("dataset/raw/faulty/sample1.csv")
    
    try:
        # Load sample data
        print("Loading normal state data...")
        normal_data = load_signal_data(normal_file)
        
        print("Loading faulty state data...")
        faulty_data = load_signal_data(faulty_file)
        
        # Generate visualizations
        print("\nGenerating visualizations...")
        
        print("1. Plotting XYZ signals for normal state...")
        plot_xyz_signals(normal_data, title="Normal State - Raw XYZ Signals")
        
        print("2. Plotting XYZ signals for faulty state...")
        plot_xyz_signals(faulty_data, title="Faulty State - Raw XYZ Signals")
        
        print("3. Plotting combined signal for normal state...")
        plot_combined_signal(normal_data, title="Normal State - Combined Signal")
        
        print("4. Plotting combined signal for faulty state...")
        plot_combined_signal(faulty_data, title="Faulty State - Combined Signal")
        
        print("5. Comparing normal and faulty states...")
        compare_normal_faulty(normal_data, faulty_data)
        
        print("\nVisualization complete!")
        
    except Exception as e:
        print(f"Error: {str(e)}")
        print("\nPlease ensure:")
        print("1. The data files exist in the specified locations")
        print("2. The CSV files have the correct column names (x_axis, y_axis, z_axis)")
        print("3. All required packages are installed")

if __name__ == "__main__":
    main() 