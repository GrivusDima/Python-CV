import cv2

# img = cv2.imread('images/photo_5240437014472100936_x.jpg')
# if img is None:
#     print("Error: Could not load image. Check the file path.")
# else:
#     img = cv2.resize(img, (500, 300))
#     cv2.imshow('image', img)
#     cv2.waitKey(0)

cap = cv2.VideoCapture('video/SmokingKills(ultimate).mp4')
while True:
    ret, frame = cap.read()
    if not ret:
        break
    resized = cv2.resize(frame, (600, 400))
    cv2.imshow('SmokingKills(ultimate)', resized)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
