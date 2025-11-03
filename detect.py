"""
detect.py
Prettified YOLOv8 object detection module with auto-save feature.
"""

import os
from datetime import datetime
import cv2
from ultralytics import YOLO
from utils import annotate_detections

def run_detection(image_path, model_name="yolov8n.pt", save_result=True, output_dir="outputs"):
    """
    Run YOLOv8 detection on an image and return the prettified annotated output.
    Auto-saves the output image with a timestamp.
    """
    print("📦 Loading YOLOv8 model...")
    model = YOLO(model_name)

    print(f"🔍 Detecting objects in: {image_path}")
    results = model(image_path)
    detections = results[0]

    # Annotate detections
    img = cv2.imread(image_path)
    annotated_img = annotate_detections(img, detections)

    if save_result:
        os.makedirs(output_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"detected_{timestamp}.jpg"
        output_path = os.path.join(output_dir, filename)
        cv2.imwrite(output_path, annotated_img)
        print(f"✅ Detection complete. Saved to: {output_path}")

    # Print detection summary
    print("\n📊 Detection Summary:")
    for box in detections.boxes:
        label = detections.names[int(box.cls[0])]
        conf = float(box.conf[0])
        print(f"🟢 {label} — confidence: {conf:.2f}")

    return img, annotated_img
