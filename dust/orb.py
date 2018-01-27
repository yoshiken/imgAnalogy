import cv2

img = cv2.imread('en2.jpg')

detector = cv2.ORB_create()

keypoints = detector.detect(img)
out = cv2.drawKeypoints(img, keypoints, None)

cv2.imshow("keypoints", out)
cv2.imwrite("orb_result.png", out)
