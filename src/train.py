from ultralytics import YOLO

def train():
    model = YOLO("yolov8n.yaml")
    model.train(
        data="data/vehiculos.yaml",
        epochs=50,
        batch=16,
        imgsz=640,
        name="yolov8_vehiculos_peligrosos"
    )

if __name__ == "__main__":
    train()
