from ultralytics import YOLO


model = YOLO("yolov8n.pt")  # build from YAML and transfer weights

# Train the model
results = model.train(data = "/data/DHRUV/MTD/YOLO/train/datasets/data.yaml", epochs = 100, imgsz = 640)