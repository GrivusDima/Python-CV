import cv2
import numpy as np
image = cv2.imread("images/PGTA_2.jpg")
print(image.shape)
# image = cv2.resize(image, (1000, 500))
image = cv2.resize(image, (image.shape[1] * 1, image.shape[0] * 1))
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(image.shape)
image = cv2.Canny(image, 100, 100) #Creates contours and Turns image colors into binary black/white
print(image.shape)

kernel = np.ones([1, 7], np.uint8) #Puts all the contours in a variable
image = cv2.dilate(image, kernel, iterations=2) #Expands light areas, written in kernel variable
image = cv2.erode(image, kernel, iterations=2) #Shrinks light areas
cv2.imwrite("images/PGTA_2.jpg", image)

cv2.imshow('PGTA 1', image)
cv2.waitKey(0)
cv2.destroyAllWindows()