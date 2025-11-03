"""
run.py
Main execution script for YOLOv8 detection with enhanced visualization.
"""

import os
from detect import run_detection
from utils import show_comparison

def main():
    print("\n🚀 YOLOv8 Object Detection — Pretty Output Edition\n")

    image_path = "sample.jpg"  # Replace with your own image path
    if not os.path.exists(image_path):
        print(f"⚠️ Image not found: {image_path}")
        return

    # Run detection
    original, detected = run_detection(image_path)

    # Display comparison
    show_comparison(original, detected, title="YOLOv8 Enhanced Detection")

if __name__ == "__main__":
    main()
