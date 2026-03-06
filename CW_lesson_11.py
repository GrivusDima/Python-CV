import numpy as np
import cv2
import os

eyecascade = cv2.CascadeClassifier('haarcascade/haarcascade_eye.xml')
face_net = cv2.dnn.readNetFromCaffe('DNN/deploy.prototxt', 'DNN/res10_300x300_ssd_iter_140000.caffemodel')

input_folder = "facepics"
output_folder = "facepics_output"

formats = ('.jpg', '.png', '.jpeg', '.webp')

os.makedirs(input_folder, exist_ok=True)
files = sorted(os.listdir(input_folder))

for file in files:
    if not file.lower().endswith(formats):
        continue

    path = os.path.join(input_folder, file)
    img = cv2.imread(path)
    if img is None:
        continue

    frame = img.copy()

    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300), (104.0, 177.0, 123.0))  # переводимо кадр в потрібний формат

    face_net.setInput(blob)  # підключаємо нейоронку
    detections = face_net.forward()  # пропускаємо кадр через нейронку
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # переводимо в гейскейл

    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]  # чому? а потому

        if confidence > 0.5:  # поріг впевненості
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])  # малюєму боксу
            (x, y, x2, y2) = box.astype("int")

            x, y = max(0, x), max(0, y)
            x2, y2 = min(w - 1, x2), min(h - 1, y2)

            cv2.rectangle(frame, (x, y), (x2, y2), (0, 255, 0), 2)

            roi_gray = gray[y:y + h, x:x + w]  # власне обличчя
            roi_color = frame[y:y + h, x:x + w]  # малюємо рамки обличчя

            eyes = eyecascade.detectMultiScale(roi_gray, 1.1, 10, minSize=(10, 10))  # шукаємо очі *в межах обличчя*

            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 2)  # малюємо рамку очей

    output_path = os.path.join(output_folder, file)
    cv2.imwrite(output_path, frame)