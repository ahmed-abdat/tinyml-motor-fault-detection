"""
Script to reformat CSV files for Edge Impulse compatibility.
Adds timestamp column and formats acceleration values for time-series data.
"""

import pandas as pd
from pathlib import Path
import sys
import numpy as np

def check_directory_exists(directory: Path, name: str) -> bool:
    """
    Check if directory exists and contains CSV files.
    """
    if not directory.exists():
        print(f"Error: {name} directory not found at {directory}")
        return False
    
    csv_files = list(directory.glob("*.csv"))
    if not csv_files:
        print(f"Warning: No CSV files found in {name} directory at {directory}")
        return False
        
    return True

def format_csv_for_edge_impulse(input_file: Path, output_file: Path):
    """
    Reformat CSV file to Edge Impulse format with timestamp and acceleration values.
    
    Args:
        input_file: Path to input CSV file
        output_file: Path to save reformatted CSV file
    """
    try:
        # Read the original CSV file
        df = pd.read_csv(input_file)
        
        # Verify the required columns exist
        required_columns = ['0', '1', '2']
        if not all(col in df.columns for col in required_columns):
            print(f"Error: File {input_file.name} missing required columns {required_columns}")
            return False
        
        # Create timestamp column (sampling at 1000Hz = 0.001s interval)
        timestamps = np.arange(0, len(df) * 0.001, 0.001)
        
        # Create new dataframe with timestamp and acceleration values
        new_df = pd.DataFrame({
            'timestamp': timestamps,
            'accX': df['0'],  # X-axis acceleration
            'accY': df['1'],  # Y-axis acceleration
            'accZ': df['2']   # Z-axis acceleration
        })
        
        # Save reformatted CSV without index
        new_df.to_csv(output_file, index=False)
        print(f"Successfully reformatted {input_file.name}")
        return True
    except Exception as e:
        print(f"Error processing {input_file.name}: {str(e)}")
        return False

def process_directory(input_dir: Path, output_dir: Path, category: str) -> int:
    """
    Process all CSV files in a directory.
    Returns number of successfully processed files.
    """
    if not check_directory_exists(input_dir, category):
        return 0
    
    success_count = 0
    total_files = len(list(input_dir.glob("*.csv")))
    print(f"\nProcessing {category} state files ({total_files} files found)...")
    
    for file in input_dir.glob("*.csv"):
        output_file = output_dir / file.name
        if format_csv_for_edge_impulse(file, output_file):
            success_count += 1
            
    return success_count

def main():
    try:
        # Create output directories if they don't exist
        base_dir = Path("dataset/edge_impulse_format")
        base_dir.mkdir(exist_ok=True)
        (base_dir / "normal").mkdir(exist_ok=True)
        (base_dir / "faulty").mkdir(exist_ok=True)
        
        # Define input directories
        healthy_dir = Path("dataset/processed/healthy")
        faulty_dir = Path("dataset/processed/faulty")
        
        # Process both directories
        healthy_count = process_directory(healthy_dir, base_dir / "normal", "healthy")
        faulty_count = process_directory(faulty_dir, base_dir / "faulty", "faulty")
        
        # Print summary
        print("\nProcessing Summary:")
        print(f"Healthy files processed: {healthy_count}")
        print(f"Faulty files processed: {faulty_count}")
        print(f"\nFiles saved in: {base_dir}")
        
        if healthy_count == 0 and faulty_count == 0:
            print("\nError: No files were processed. Please check your input directories:")
            print(f"Healthy directory: {healthy_dir}")
            print(f"Faulty directory: {faulty_dir}")
            sys.exit(1)
            
        print("\nNext steps:")
        print("1. Go to Edge Impulse Data Acquisition")
        print("2. Click 'Upload data'")
        print("3. Select files from dataset/edge_impulse_format/normal or faulty")
        print("4. Set appropriate label (normal/faulty)")
        print("5. Enable 'Automatically split between training and testing'")
        print("6. When asked, select 'Yes, this is time-series data'")
        
    except Exception as e:
        print(f"\nError: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 