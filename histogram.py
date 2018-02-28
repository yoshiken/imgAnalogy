# -*- coding: UTF-8 -*-

import cv2
import matplotlib.pyplot as plt
import sys
import os

def imgurl():
    IMG_DIR = os.path.abspath(os.path.dirname(__file__)) + '/imgdataset/'
    files = os.listdir(IMG_DIR)
    return files

def compare_by_hist():
    args = sys.argv
    file = imgurl()
    TARGET_FILE = args[1]
    for i in file:
        if not i == '.DS_Store':
	        COMPARING_FILE = 'imgdataset/' + i
	        IMG_SIZE = (200, 200)

	        #比較するイメージファイルを読み込み、ヒストグラムを計算
	        target_img_path = TARGET_FILE
	        target_img = cv2.imread(target_img_path)
	        target_img = cv2.resize(target_img, IMG_SIZE)
	        target_hist = cv2.calcHist([target_img], [0], None, [256], [0, 256])

	        #比較されるイメージファイルを読み込み、ヒストグラムを計算
	        comparing_img_path = COMPARING_FILE
	        comparing_img = cv2.imread(comparing_img_path)
	        comparing_img = cv2.resize(comparing_img, IMG_SIZE)
	        comparing_hist = cv2.calcHist([comparing_img], [0], None, [256], [0, 256])

	        #ヒストグラムを比較する
	        result = cv2.compareHist(target_hist, comparing_hist, 0)
	        print(i + "," + str(result))

if __name__ == '__main__':
	compare_by_hist()
