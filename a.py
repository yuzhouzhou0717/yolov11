from ultralytics import YOLO

# Load a pretrained YOLOv8n model
model = YOLO("yolov8n.pt")

# Define path to the image file
source = "E:\Agriculture\\ultralytics-main\\ultralytics\\assets\\bus.jpg"

# Run inference on the source
results = model(source,save=True)  # list of Results objects

