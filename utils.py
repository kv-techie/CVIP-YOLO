"""
utils.py
Utility functions for image handling and visualization.
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

def load_image(path):
    """Load an image using OpenCV."""
    img = cv2.imread(path)
    if img is None:
        raise FileNotFoundError(f"❌ Image not found at {path}")
    return img

def show_comparison(original, detected, title="YOLOv8 Detection Result"):
    """Display original and detected images side by side."""
    fig, axs = plt.subplots(1, 2, figsize=(14, 6))
    axs[0].imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))
    axs[0].set_title("Original Image", fontsize=14, fontweight='bold')
    axs[0].axis("off")

    axs[1].imshow(cv2.cvtColor(detected, cv2.COLOR_BGR2RGB))
    axs[1].set_title(title, fontsize=14, fontweight='bold')
    axs[1].axis("off")

    plt.tight_layout()
    plt.show()

def annotate_detections(img, detections):
    """
    Draws bounding boxes, labels, and confidence scores on the image.
    Uses YOLO detection results.
    """
    annotated = img.copy()
    for box in detections.boxes:
        cls_id = int(box.cls[0])
        label = detections.names[cls_id]
        conf = float(box.conf[0])
        x1, y1, x2, y2 = map(int, box.xyxy[0])

        color = (0, 255, 0)  # green box
        cv2.rectangle(annotated, (x1, y1), (x2, y2), color, 2)

        # Label text background
        label_text = f"{label} ({conf:.2f})"
        (text_w, text_h), _ = cv2.getTextSize(label_text, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)
        cv2.rectangle(annotated, (x1, y1 - text_h - 8), (x1 + text_w + 2, y1), color, -1)
        cv2.putText(annotated, label_text, (x1 + 2, y1 - 4),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
    return annotated
