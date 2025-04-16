"""
Constants and configuration parameters for vibration signal visualization.
"""

# Data paths
RAW_DATA_PATH = "dataset/raw"
PROCESSED_DATA_PATH = "dataset/processed"

# Signal parameters
SAMPLING_RATE = 1000  # Hz
SIGNAL_DURATION = 5  # seconds
SAMPLES_PER_SIGNAL = SAMPLING_RATE * SIGNAL_DURATION

# Visualization parameters
FIGURE_SIZE = (12, 6)
DPI = 100
COLORS = {
    'normal': '#2ecc71',  # Green
    'faulty': '#e74c3c',  # Red
    'grid': '#95a5a6',    # Gray
    'background': '#ffffff'  # White
}

# Labels
LABELS = {
    'time': 'Time (s)',
    'amplitude': 'Amplitude (g)',
    'frequency': 'Frequency (Hz)',
    'normal': 'Normal State',
    'faulty': 'Faulty State'
} 