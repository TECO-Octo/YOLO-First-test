import os
from ultralytics import YOLO
from python_modules.video_converter import convert_video
from python_modules.user_interaction import ask_overwrite
from python_modules.file_handler import prepare_files_for_conversion

# Load a pretrained YOLO model
model = YOLO('models/pytorch/yolov8n.pt')

source = "https://www.youtube.com/watch?v=e_WBuBqS9h8"

# Perform object detection on an image using the model
results = model(source,
                conf=0.6,
                iou=0.7,
                device="cpu",
                show=True,
                save=True,
                stream=True
                )
for r in results:
    boxes = r.boxes  # Boxes object for box outputs
    masks = r.masks  # Masks object for segment masks outputs
    probs = r.probs  # Class probabilities for classification outputs

base_dir = 'runs/detect'
output_dir = 'export/mp4'
os.makedirs(output_dir, exist_ok=True)

# Prepare files for conversion
files_to_convert = prepare_files_for_conversion(base_dir, output_dir, ask_overwrite)

# Perform the conversion
for input_path, output_path in files_to_convert:
    convert_video(input_path, output_path)
