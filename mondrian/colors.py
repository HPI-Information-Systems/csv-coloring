import cv2 as cv
import numpy as np

# https://www.imgonline.com.ua/eng/color-palette.php
from webcolors import hex_to_rgb

RGB_BLACK = np.asarray([0, 0, 0])
RGB_WHITE = np.asarray([255, 255, 255])
RGB_SPRINGGREEN = np.asarray([0,255,127])
RGB_LIME = np.asarray([0,255,0])
RGB_LIGHTGREEN = np.asarray([144,238,144])
RGB_LIMEGREEN = np.asarray([50,205,50])
RGB_DARKPINK = np.asarray([255, 99, 123])
RGB_MEDIUMORCHID = np.asarray([186,85,211])
RGB_MEDIUMPURPLE = np.asarray([186,85,211])
RGB_LIGHTPINK = np.asarray([255,182,193])

HSV_BLACK = cv.cvtColor(np.uint8([[RGB_BLACK]]), cv.COLOR_RGB2HSV)
HSV_WHITE = cv.cvtColor(np.uint8([[RGB_WHITE]]), cv.COLOR_RGB2HSV)
HSV_RED = cv.cvtColor(np.uint8([[RGB_SPRINGGREEN]]), cv.COLOR_RGB2HSV)
HSV_GREEN = cv.cvtColor(np.uint8([[RGB_MEDIUMPURPLE]]), cv.COLOR_RGB2HSV)
HSV_BLUE = cv.cvtColor(np.uint8([[RGB_DARKPINK]]), cv.COLOR_RGB2HSV)

hex_region_colors = ['#51933a', '#9c5c2c', '#6686e2', '#9b7f30', '#317341', '#d7407e', '#a9b365', '#825bcd', '#c58cd6', '#91ba35', '#42c0c7',
                     '#657028', '#d1522b', '#c853b8', '#5dc99c', '#e1936a', '#b35659', '#e385a5', '#54c25e', '#6160a3', '#9c4b7b', '#419a76',
                     '#5f9fd3', '#d34250', '#d7a135']
