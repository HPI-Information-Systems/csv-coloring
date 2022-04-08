import csv
import pandas as pd
import os
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageEnhance
import streamlit as st
import json

import sys
sys.path.append('C:\\Users\\Ella\\Ella-Kopie\\Studium\\Semester9\\Job\\Mondrian extension for CSV Visualization\\mondrian')
from parsing import parse_cell

import os

with open("C:\\Users\\Ella\\Ella-Kopie\\Studium\\Semester9\\Job\\Mondrian extension for CSV Visualization\\mondrian\\colors.json", "r") as jsonfile:
    data = json.load(jsonfile) # Reading the file
    jsonfile.close()

@st.cache(ttl= 24*3600, max_entries= 20) 
def table_as_image_better(path, dialect= 'excel', color=True, cell_length=False, config_file_data=data,**formatparams ):
    data = config_file_data
    img = []
    last_nonempty = 0
    # this checks whether file is empty or not
    #if the file is empty, we want to just give out a white rectangle
    if os.stat(path).st_size==0:
        st.write("You entered an empty file.")
        img= [[(255,255,255)]]
        return img
    with open(path, 'r', encoding="UTF-8", errors="ignore") as csvfile:
        tablereader = csv.reader(csvfile, dialect,**formatparams)
        max_size = 0

        #the following part of the code ensures that even csv files with huge data cells can be read
       
        maxInt = sys.maxsize

        while True:
            # decrease the maxInt value by factor 10 
            # as long as the OverflowError occurs.

            try:
                csv.field_size_limit(maxInt)
                break
            except OverflowError:
                maxInt = int(maxInt/10)
                
        img, last_nonempty, max_size = parse_file(tablereader, cell_length,color)

    img = img[:last_nonempty + 1][:]

    new_img = []

    # basically, i want to mark the lines with a rim that have lesser length than others by adding white
    # space in the parts that are left over compared to other lines  

    with open("C:\\Users\\Ella\\Ella-Kopie\\Studium\\Semester9\\Job\\Mondrian extension for CSV Visualization\\mondrian\\colors.json", "r") as jsonfile:
        data = json.load(jsonfile) # Reading the file
        jsonfile.close()

    for idx, line in enumerate(img):

        new_line=[]
        for val in line:

            val = [255* val[0], 255* val[1], 255* val[2]]
            new_line.append(val)

        line=new_line
        line += [[255, 255, 255]] * (max_size - len(line))
        new_img.append(line)
        if str(data['separator_rows'])=='True':

            line = [[0,0,0]]*max_size
            new_img.append(line)

    with open("colors.json", "w") as jsonfile:
        json.dump(data, jsonfile)
        jsonfile.close()

    img= new_img

    return img
    

def parse_file(csv_reader, cell_length, color):
    img = []
    max_size = 0
    last_nonempty=0

    with open("C:\\Users\\Ella\\Ella-Kopie\\Studium\\Semester9\\Job\\Mondrian extension for CSV Visualization\\mondrian\\colors.json", "r") as jsonfile:
        data = json.load(jsonfile) # Reading the file
        jsonfile.close()

    for idx, line in enumerate(csv_reader):
    #loop for identifying last nonempty line + for parsing the colors of each line that reader reads

        if line != [''] * len(line):
            last_nonempty = idx

        # we are incrasing the idx by 1 because the numbering of the lines starts at 1 in the file but 
        # the idx starts at 0

        #here, we choose the lines whose colors are displayed in the app
        if data['row_output_from'] !=0:
            if idx+1 < data['row_output_from']:
                continue
        
        if data['row_output_until'] !=0:
            if idx+1 > data['row_output_until']:
                break
                	
        result = [parse_cell(val=val, color=color) for val in line]

        #cell_length creates image where columns are sized according to the size of their content
        if cell_length:
            result = [r for idx, r in enumerate(result) for _ in range(len(line[idx]))]

        if len(result) > max_size:
            max_size = len(result)

        img.append(result)
        #loop ends

    return img,last_nonempty, max_size

#img_same regulates whether pictures with one color are shown in the output or not
def manipulate_created_image(img_file, image_same=True, resampling_method = "Nearest-neighbor  Interpolation"):
    with open("C:\\Users\\Ella\\Ella-Kopie\\Studium\\Semester9\\Job\\Mondrian extension for CSV Visualization\\mondrian\\colors.json", "r") as jsonfile:
        data = json.load(jsonfile) # Reading the file
        jsonfile.close()

    img_colors_all_same = False
    if image_same:
        img_colors_all_same = check_if_image_same(img_file)

    img = np.array(img_file,dtype=np.int8)
    img_file = Image.fromarray(img, 'RGB')
    img_file = use_resampling_algorithm(img_file, resampling_method)
    enhancer = ImageEnhance.Brightness(img_file)
    factor = 0.97
    img_file = enhancer.enhance(factor)

    return img_colors_all_same,img_file

def use_resampling_algorithm(img_file, resampling_method):
    with open("C:\\Users\\Ella\\Ella-Kopie\\Studium\\Semester9\\Job\\Mondrian extension for CSV Visualization\\mondrian\\colors.json", "r") as jsonfile:
        data = json.load(jsonfile) # Reading the file
        jsonfile.close()

    if resampling_method=="Bilinear algorithm":
        img_file = img_file.resize((data['width'], data['height']), resample=Image.BILINEAR)

    elif resampling_method=="Bicubic algorithm":
        img_file = img_file.resize((data['width'], data['height']), resample=Image.BICUBIC)

    elif resampling_method=="Box Sampling":
        img_file = img_file.resize((data['width'], data['height']), resample=Image.BOX)

    elif resampling_method=="Lanczos Resampling":
        img_file = img_file.resize((data['width'], data['height']), resample=Image.LANCZOS)

    elif resampling_method=="Hamming algorithm":
        img_file = img_file.resize((data['width'], data['height']), resample=Image.HAMMING)

    #We are taking the Nearest-Neighbor Interpolation as the default
    else:
        img_file = img_file.resize((data['width'], data['height']), resample=Image.NEAREST)
    
    return img_file

#checks if there are at least two pixels with different colors in an image
def check_if_image_same(img_file):
    img_colors_all_same = True
    if len(img_file)==0:
        return img_colors_all_same
    first_element = img_file[0][0]
    for list in img_file:
        for element in list:
            if first_element != element:
                img_colors_all_same = False
                return img_colors_all_same
    return img_colors_all_same






