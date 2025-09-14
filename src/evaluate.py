from ultralytics import YOLO

def evaluate():
    model = YOLO("models/yolov8.pt")
    metrics = model.val()
    print(metrics)

if __name__ == "__main__":
    evaluate()
