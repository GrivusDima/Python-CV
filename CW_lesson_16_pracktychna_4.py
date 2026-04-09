# Відео дорож руху, порахувати кількість машин
import os
import cv2
import time
from ultralytics import YOLO

PROJECT_DIR = os.path.dirname(__file__)
VIDEO_DIR = os.path.join(PROJECT_DIR, 'videos')
OUT_DIR = os.path.join(PROJECT_DIR, 'output')
CAR_CLASS_ID = 2

os.makedirs(OUT_DIR, exist_ok=True)

video_path = os.path.join(VIDEO_DIR, 'Cars Moving On Road Stock Footage - Free Download.mp4')
cap = cv2.VideoCapture(video_path)

model = YOLO("yolo26n.pt")

CONF_THRESHOLD = 0.5

RESIZE_WIDTH = 960

prev_time = time.time()
fps = 0.0

car_count = 0
pseudo_id = 0

def detect_cars(image):
    global car_count, pseudo_id, CAR_CLASS_ID
    results = model(frame, conf=CONF_THRESHOLD, verbose=False)
    for detection in results[0].boxes:
        class_id = int(detection.cls)
        label = model.names[class_id]
        if label.lower() == "car" or label.lower() == "bus" or label.lower() == "truck":
            x1, y1, x2, y2 = map(int, detection.xyxy[0])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)

    for r in results:
        boxes = r.boxes
        if boxes is None:
            continue

        for box in boxes:
            cls = int(box.cls[0])
            conf = float(box.conf[0])

            x1, y1, x2, y2 = map(int, box.xyxy[0])
            if cls == CAR_CLASS_ID:
                if ((y1+y2)/2 >= frame.shape[0]-300 and (y2+y1)/2 <= frame.shape[0]-290):
                    car_count += 1
                    pseudo_id += 1

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

                label = f'id: {pseudo_id} conf: {conf:.2f}'
                cv2.putText(frame, label, (x1, y1), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 0, 255), 2)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if RESIZE_WIDTH is not None:
        h, w = frame.shape[:2]
        scale = RESIZE_WIDTH / w
        new_w = RESIZE_WIDTH
        new_h = int(h * scale)

        frame = cv2.resize(frame, (new_w, new_h))

    detect_cars(frame)

    cv2.line(frame, (0, frame.shape[0]-300), (frame.shape[1], frame.shape[0]-300), (0, 255, 0), 2)
    cv2.putText(frame, f'Car count: {car_count}', (50, 50), cv2.FONT_HERSHEY_TRIPLEX, 1.2, (0, 255, 255), 2)
    cv2.imshow('YOLO', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#