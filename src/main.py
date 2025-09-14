import cv2
from ultralytics import YOLO

def main():
    model = YOLO("models/yolov8.pt")
    cap = cv2.VideoCapture("videos/test.mp4")
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        results = model(frame)
        annotated_frame = results[0].plot()
        cv2.imshow("Detección Vehículos Peligrosos", annotated_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
