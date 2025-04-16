"""
Utility functions for vibration signal analysis and visualization.
"""

import numpy as np
import pandas as pd
from pathlib import Path
from typing import Tuple, List, Dict
from .constants import *

def load_signal_data(file_path: str) -> pd.DataFrame:
    """
    Load vibration signal data from CSV file.
    
    Args:
        file_path: Path to the CSV file containing vibration data
        
    Returns:
        DataFrame with X, Y, Z acceleration columns
    """
    try:
        df = pd.read_csv(file_path)
        required_columns = ['x_axis', 'y_axis', 'z_axis']
        if not all(col in df.columns for col in required_columns):
            raise ValueError(f"CSV must contain columns: {required_columns}")
        return df
    except Exception as e:
        print(f"Error loading data from {file_path}: {str(e)}")
        raise

def combine_xyz_signals(x: np.ndarray, y: np.ndarray, z: np.ndarray) -> np.ndarray:
    """
    Combine X, Y, Z acceleration signals into a composite signal.
    
    Args:
        x: X-axis acceleration values
        y: Y-axis acceleration values
        z: Z-axis acceleration values
        
    Returns:
        Combined signal array
    """
    return np.sqrt(x**2 + y**2 + z**2)

def normalize_signal(signal: np.ndarray) -> np.ndarray:
    """
    Normalize signal by dividing by maximum amplitude.
    
    Args:
        signal: Input signal array
        
    Returns:
        Normalized signal array
    """
    max_amp = np.max(np.abs(signal))
    return signal / max_amp if max_amp != 0 else signal

def generate_time_axis(n_samples: int) -> np.ndarray:
    """
    Generate time axis array based on sampling rate.
    
    Args:
        n_samples: Number of samples in the signal
        
    Returns:
        Time axis array
    """
    return np.linspace(0, SIGNAL_DURATION, n_samples) 