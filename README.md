# Path Detection and Sequence Generation

This project detects red, green, and blue points in an image and generates a path sequence based on their positions. It uses OpenCV for image processing and is written in Python.

## Features
- Detects red (start), green (end), and blue (turn) points.
- Generates a path sequence indicating movement directions.
- Provides detailed debugging and error handling.

## Prerequisites
Ensure you have the following installed:
- **Python 3.8+**
- **pip (Python package manager)**

## Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/path-detection.git
   cd path-detection
   ```
2. **Create Virtual Environments**
    ```
    python3 -m venv venv
    source venv/bin/activate   # On Linux/Mac
    venv\Scripts\activate      # On Windows
    ```
```bash
# Install OpenCV and NumPy manually 
pip install opencv-python-headless numpy

# Update the image path in the script
image_path = "/path/to/your/image.jpg"

# Run the main script
python script.py

