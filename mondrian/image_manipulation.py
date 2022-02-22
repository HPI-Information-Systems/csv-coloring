import csv
import pandas as pd
import os
import pickle
import random
import PIL
from pathlib import Path

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageEnhance


def manipulate_created_image(img_file, width=200, height=200):
        img_file = img_file.resize((width, height))

        # Decreaase brightness of image -> White parts (empty cells) will still be visible on white 
        
        enhancer = ImageEnhance.Brightness(img_file)
        factor = 0.97
        img_file = enhancer.enhance(factor)

        return img_file