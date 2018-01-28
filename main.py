import numpy as np
import cv2
import os
import sys


def imgurl():
    IMG_DIR = os.path.abspath(os.path.dirname(__file__)) + '/imgdataset/'
    files = os.listdir(IMG_DIR)
    return files 


def detectorcall():
    # AgastFeatureDetector
    #detector = cv2.AgastFeatureDetector_create()

    # FAST
    #detector = cv2.FastFeatureDetector_create()

    # MSER
    #detector = cv2.MSER_create()

    # AKAZE
    #detector = cv2.AKAZE_create()

    # BRISK
    #detector = cv2.BRISK_create()

    # KAZE
    #detector = cv2.KAZE_create()

    # ORB (Oriented FAST and Rotated BRIEF)
    #detector = cv2.ORB_create()

    # SimpleBlobDetector
    #detector = cv2.SimpleBlobDetector_create()

    # SIFT
    detector = cv2.xfeatures2d.SIFT_create()

    return detector 

args = sys.argv

img1 = cv2.imread(args[1],0)
#img2 = cv2.imread('./imgdataset/obj3__28.png',0)
file =imgurl()
detector = detectorcall()

for i in file:
    if not i == '.DS_Store':
        img2 = cv2.imread('./imgdataset/' + i,0)
        kp1, des1 = detector.detectAndCompute(img1, None)
        kp2, des2 = detector.detectAndCompute(img2, None)

        bf = cv2.BFMatcher()
        matches = bf.knnMatch(des1,des2, k=2)

        good = []
        ret = 0
        c = 0
        match_param = 2
        for m,n in matches:
            c +=1
            ret += m.distance
            if m.distance < match_param*n.distance:
                good.append([m])
        print(i + "," + str(ret/c))
        #img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good, None,flags=2)

#後処理
#cv2.imwrite("shift_result.png", img3)
#cv2.imshow("shit_result",img3)
#cv2.waitKey(0)
#print(type(matches))
