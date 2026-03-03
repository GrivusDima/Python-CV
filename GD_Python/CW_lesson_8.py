import cv2
import numpy as np
facecascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
eyecascade = cv2.CascadeClassifier('haarcascade/haarcascade_eye.xml')
mouthcascade = cv2.CascadeClassifier('haarcascade/haarcascade_smile.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #переводимо в гейскейл

    faces = facecascade.detectMultiScale(gray, 1.1, 5, minSize=(10,30)) #аналізуємо зображення на предмет лиць

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2) #перебирання кожного обиччя

        roi_gray = gray[y:y + h, x:x + w] #власне обличчя
        roi_color = frame[y:y + h, x:x + w] #малюємо рамки обличчя


        eyes = eyecascade.detectMultiScale(roi_gray, 1.1, 10, minSize=(10,10)) #шукаємо очі *в межах обличчя*

        for(ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 2) #малюємо рамку очей


        mouth = mouthcascade.detectMultiScale(roi_gray, 1.1, 10, minSize=(16,30))

        for (mx, my, mw, mh) in mouth:
            cv2.rectangle(roi_color, (mx, my), (mx + mw, my + mh), (0, 255, 0), 2) #малюємо рамку moutgh

    cv2.putText(frame, f'Faces detected: {len(faces)}', (10,30), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0), 2)

    cv2.imshow('Haar Face Thingy', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()