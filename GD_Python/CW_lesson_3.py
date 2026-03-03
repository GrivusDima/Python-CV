import cv2
import numpy as np
from numpy.ma.core import filled

img = np.zeros((300, 300, 3), np.uint8)
# img[100:150,200:280] = 50,250,100
#img[:] = 100,250,100

print(img.shape)
cv2.line(img, (0, img.shape[0]//2), (img.shape[1], img.shape[0]//2), (255,255,255), 2)

cv2.circle(img, (200, 200), 25, (255,255,255), 2)
cv2.circle(img, (100, 100), 25, (255,255,255), 2)

#cv2.rectangle(img, (250,250), (300,300), (200,200,200), -1)
cv2.rectangle(img, (100,100), (200,200), (50,255,100), 2)
cv2.rectangle(img, (150,50), (250,150), (50,255,100), 2)

cv2.line(img, (200,200), (250,150), (50,255,100), 2)
cv2.line(img, (100,100), (150,50), (50,255,100), 2)
cv2.line(img, (200,100), (250,50), (50,255,100), 2)
cv2.line(img, (100,200), (150,150), (50,255,100), 2)

cv2.putText(img, "YO WASSUP WORLD", (100, 250), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()