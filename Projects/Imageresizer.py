import cv2
image = cv2.imread("shiv.jpeg", cv2.IMREAD_UNCHANGED)
cv2.imshow("title", image)
cv2.waitKey(0)