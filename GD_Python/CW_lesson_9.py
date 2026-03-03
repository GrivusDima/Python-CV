import cv2
import numpy as np

# facecascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
# eyecascade = cv2.CascadeClassifier('haarcascade/haarcascade_eye.xml')
# mouthcascade = cv2.CascadeClassifier('haarcascade/haarcascade_smile.xml')

face_net = cv2.dnn.readNetFromCaffe('DNN/deploy.prototxt', 'DNN/res10_300x300_ssd_iter_140000.caffemodel')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    #--------------------DNN--------------------#

    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300), (104.0, 177.0, 123.0)) #переводимо кадр в потрібний формат

    face_net.setInput(blob) #підключаємо нейоронку
    detections = face_net.forward() #пропускаємо кадр через нейронку

    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2] #чому? а потому

        if confidence > 0.5: #поріг впевненості
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h]) #малюєму боксу
            (x, y, x2, y2) = box.astype("int")

            x, y = max(0, x), max(0, y)
            x2, y2 = min(w-1, x2), min(h-1, y2)

            cv2.rectangle(frame, (x, y), (x2, y2), (255, 0, 0), 2)

    cv2.imshow("SHOW YO FACE (CLANKER)", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

    #--------------------DNN--------------------#

    #----------------HaarCascade-----------------#

    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #переводимо в гейскейл
    #
    # faces = facecascade.detectMultiScale(gray, 1.1, 5, minSize=(10,30)) #аналізуємо зображення на предмет лиць
    #
    # for (x, y, w, h) in faces:
    #     cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2) #перебирання кожного обиччя
    #
    #     roi_gray = gray[y:y + h, x:x + w] #власне обличчя
    #     roi_color = frame[y:y + h, x:x + w] #малюємо рамки обличчя
    #
    #
    #     eyes = eyecascade.detectMultiScale(roi_gray, 1.1, 10, minSize=(10,10)) #шукаємо очі *в межах обличчя*
    #
    #     for(ex, ey, ew, eh) in eyes:
    #         cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 2) #малюємо рамку очей
    #
    #
    #     mouth = mouthcascade.detectMultiScale(roi_gray, 1.1, 10, minSize=(16,30))
    #
    #     for (mx, my, mw, mh) in mouth:
    #         cv2.rectangle(roi_color, (mx, my), (mx + mw, my + mh), (0, 255, 0), 2) #малюємо рамку moutgh
    #
    # cv2.putText(frame, f'Faces detected: {len(faces)}', (10,30), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0), 2)
    #
    # cv2.imshow('SHOW YO FACE (PUNK)', frame)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break
#
# cap.release()
# cv2.destroyAllWindows()

# --------------------HaarCascade--------------------#