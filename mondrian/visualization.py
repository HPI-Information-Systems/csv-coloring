import csv
import pandas as pd
import os
import pickle
import random
import PIL
from pathlib import Path
import colour
import math
#import pdb

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter
import streamlit as st
import json

#import streamlit as st
#from streamlit import colors as colors
#import streamlit.colors as colors
#from . import colors as colors
#import colour as colors
#from .parsing import parse_cell
import sys
sys.path.append('C:\\Users\\Ella\\Ella-Kopie\\Studium\\Semester9\\Job\\Mondrian extension for CSV Visualization\\mondrian')
#sys.path.append("C:\\Users\\Ella\\Ella-Kopie\\Studium\\Semester9\\Job\Mondrian extension for CSV Visualization\\mondrian\\parsing.py")
#import parsing
from parsing import parse_cell
#from .partition import find_external_lines, partition_contour, find_virtual_lines
from partition import find_external_lines, partition_contour, find_virtual_lines
import clevercsv

import os
def table_as_image_better(path, dialect= 'excel', color=True, cell_length=False, **formatparams):
    #print("starting function")
    img = []
    last_nonempty = 0
    #print(color)
    line=""
    # this checks whether file is empty or not
    #if the file is empty, we want to just give out a white rectangle
    if os.stat(path).st_size==0:
        st.write("You entered an empty file.")
        img= [[(255,255,255)]]
        return img
    #st.write(str(formatparams))
    with open(path, 'r', encoding="UTF-8", errors="ignore") as csvfile:
        #print('start reading')
        tablereader = csv.reader(csvfile, dialect,**formatparams)
        st.write(tablereader)
        max_size = 0

        #the following part of the code ensures that even csv file swith huge fields can be read
        maxInt = sys.maxsize

        while True:
            # decrease the maxInt value by factor 10 
            # as long as the OverflowError occurs.

            try:
                csv.field_size_limit(maxInt)
                break
            except OverflowError:
                #TODO: Find out if we are only using this one in case includes taht you have to input a certain number of files at the start of an OverflowError
                #st.write("OverflowError")
                #st.write(maxInt)
                maxInt = int(maxInt/10)
                
            
            for idx, line in enumerate(tablereader):
                    if line != [''] * len(line):
                        last_nonempty = idx

            #TODO: maybe move the programm that on demand only gives out certain amount of rows/columns
            # here so that we do not waste any tim parsing them!?
            #print(line)
            result = [parse_cell(val=val, color=color) for val in line]
            #st.write(result)
            if cell_length:
                result = [r for idx, r in enumerate(result) for _ in range(len(line[idx]))]

            if len(result) > max_size:
                max_size = len(result)

            img.append(result)

    img = img[:last_nonempty + 1][:]

    #print(max_size)
    #st.write(img)

    new_img = []
    #TODO: Apply multiplication with 255 to files with uneve length as well

    #basically, i want to mark the parts with a rim that have lesser length than others by adding white
    # space in the parts that are left overcompared to other lines  

    with open("C:\\Users\\Ella\\Ella-Kopie\\Studium\\Semester9\\Job\\Mondrian extension for CSV Visualization\\mondrian\\colors.json", "r") as jsonfile:
        data = json.load(jsonfile) # Reading the file
        #print("Read successful")
        jsonfile.close()

    # pandas_img = pd.DataFrame(img)
    # #print(pandas_img)
    # print(len(pandas_img.columns))

    # if data['column_output_start'] != 0 :
    #     pandas_img = pandas_img[:, data['column_output_start']-1: ]
    # if data['column_output_end'] != 0| (data['column_output_from']==0 & data['column_output_until']!=0) :
    #     #should this not result in 
    #     pandas_img = pandas_img[:, :data['column_output_end']-1]

    # if data['column_output_from']!=0 & data['column_output_until']!=0:
    #         #in this part we are adapting the given row numbers to row numbers of the file according to dialect
    #         if data['column_output_from']> len(pandas_img.columns):
    #             st.write("The file as read by the given dialect has fewer rows than the row number given as the output start. We will try"
    #             +'to diplay an approximate selection from the file')

    #             difference = data['column_output_from']/data['column_output_until']
    #             adapted_start_row = math.ceil(difference * len(pandas_img.columns))
    #             # data['column_output_from'] = adapted_start_row
    #             # data['column_output_until'] = len(pandas_img.columns)-1
    #             pandas_img= pandas_img.loc[:,adapted_start_row: len(pandas_img.columns)-1]
    #         elif data['column_output_until']> len(img):
    #             st.write("The file as read by the given dialect has fewer rows than the row number given as the output end. We will try"
    #             +'to diplay an approximate selection from the file')
    #             difference = data['column_output_until'] -(len(pandas_img.columns)-1)
    #             pandas_img= pandas_img.loc[:,math.max(0, data['column_output_from'])-difference: len(pandas_img.columns)-1]
    #             # data['column_output_from'] = math.max(0, data['column_output_from']-difference )
    #             # data['column_output_until'] = len(pandas_img.columns)-1
                
    #         if 0 < data['column_output_from']:
    #             pandas_img= pandas_img.loc[:,data['column_output_from']-1 ]          

    #         if len(pandas_img.columns)> data['column_output_until']:
    #             pandas_img = pandas_img.loc[:, :data['column_output_until']-1]
    
    # if img !=pandas_img.to_numpy():
    #     img = pandas_img.to_numpy()
    #breakpoint()
    #pdb.set_trace()

    line_number = 0
    for idx, line in enumerate(img):
        #line += [[255, 255, 255]] * (max_size - len(line))

        #here we are using the user inputs about what lines are to be chosen exactly
        
        #TODO: Do compute the following stuff in a way so that it does not have to be recomputed in every loop instance
        #this case includes that you have to output a certain number of files at the start + when there are given numbers
        #for the row where the output starts + the number of the row where the output ends but where line where the output is supposed to start
        #TODO:Figure out what he 2md part of the case means
        if data['row_output_start'] != 0:
            if line_number> data['row_output_start']:
                line_number = line_number +1
                continue
        if data['row_output_end'] != 0  | (data['row_output_from']==0 & data['row_output_until']!=0):
            if len(img)-line_number <= data['row_output_end']:
                line_number = line_number +1
                continue

        if data['row_output_from']!=0 & data['row_output_until']!=0:
            #in this part we are adapting the given row numbers to row numbers of the file according to dialect
            if data['row_output_from']> len(img):
                st.write("The file as read by the given dialect has fewer rows than the row number given as the output start. We will try"
                +'to diplay an approximate selection from the file')

                st.write("row_output_from: " + data['row_output_from'])
                st.write("row_output_until: " + data['row_output_untiil'])
                difference = data['row_output_from']/data['row_output_until']
                adapted_start_row = math.ceil(difference * len(img))
                st.write("difference: "+ difference + " adapted_start_row: "+adapted_start_row)
                data['row_output_from'] = adapted_start_row
                data['row_output_until'] = len(img)-1
                st.write("row_output_from: " + data['row_output_from'])
                st.write("row_output_until: " + data['row_output_untiil'])
            elif data['row_output_until']> len(img):
                st.write("The file as read by the given dialect has fewer rows than the row number given as the output end. We will try"
                +'to diplay an approximate selection from the file')
                difference = data['row_output_until'] -(len(img)-1)
                data['row_output_from'] = math.max(0, data['row_output_from']-difference )
                data['row_output_until'] = len(img)-1
                
            if line_number< data['row_output_from']:
                line_number = line_number +1
                continue

            if line_number> data['row_output_until']:
                line_number = line_number +1
                continue

        #we are now implementing the command that a certain portion of all rows in the 'middle'
        # of the image is supposed to be diplayed - if the row numbers given are too high, then we will display the proportionate amount of lines
        # from the real amount of the real amount of rows
        new_line=[]
        val_num=0
        for val in line:
            # #print(val)
            # if data['column_output_start'] != 0 :
            #     if val_num> data['column_output_start']:
            #         val_num = val_num+1
            #         max_size = max_size - data['column_output_start']                 
            #         continue
            # if data['column_output_end'] != 0| (data['column_output_from']==0 & data['column_output_until']!=0) :
            #     if len(line)-val_num <= data['column_output_end']:
            #         val_num = val_num+1    
            #         max_size = data['column_output_end']      
            #         continue

            # if data['column_output_from']!=0 & data['column_output_until']!=0:
            #     #in this part we are adapting the given row numbers to row numbers of the file according to dialect
            #     if data['column_output_from']> len(line):
            #         st.write("The file as read by the given dialect has fewer rows than the row number given as the output start. We will try"
            #         +'to diplay an approximate selection from the file')

            #         st.write("column_output_from: " + data['column_output_from'])
            #         st.write("column_output_until: " + data['column_output_untiil'])

            #         difference = data['column_output_from']/data['column_output_until']
            #         adapted_start_row = math.ceil(difference * len(line))
            #         st.write("difference: "+ difference + " adapted_start_row: "+adapted_start_row)
            #         data['column_output_from'] = adapted_start_row
            #         data['column_output_until'] = len(line)-1
            #         st.write("column_output_from: " + data['column_output_from'])
            #         st.write("column_output_until: " + data['column_output_untiil'])
            #         val_num = val_num+1                    
            #     elif data['column_output_until']> len(img):
            #         st.write("The file as read by the given dialect has fewer rows than the row number given as the output end. We will try"
            #         +'to diplay an approximate selection from the file')
            #         difference = data['column_output_until'] -(len(img)-1)
            #         data['column_output_from'] = math.max(0, data['column_output_from']-difference )
            #         data['column_output_until'] = len(img)-1
            #         val_num = val_num+1   
            #         max_size = ['column_output_until']- ['column_output_from']
                                 
                    
            # if val_num< data['column_output_from']:
            #     val_num = val_num+1                    
            #     continue

            # if val_num> data['column_output_until']:
            #     val_num = val_num+1                    
            #     continue


            val = [255* val[0], 255* val[1], 255* val[2]]
            new_line.append(val)
            #print(val)
            # if val == len(line)-1:
            #     val_num = 0
            # else:
            #     val = val+1
        line=new_line
        #print(max_size-len(line))
        line += [[255, 255, 255]] * (max_size - len(line))
        #st.write(line)
        new_img.append(line)
        line_number= line_number + 1

    with open("colors.json", "w") as jsonfile:
        myJSON = json.dump(data, jsonfile) # Writing to the file
        #print("Write successful")
        jsonfile.close()

    img= new_img

    return img
    
    #moved this part to its own file for more control over image properties lik size
    
def manipulate_created_image_deprecated(img_file):
    img_file = img_file.resize((200, 200), resample=Image.NEAREST)
    print(img_file)
    # Decreaase brightness of image -> White parts (empty cells) will still be visible on white 
    
    enhancer = ImageEnhance.Brightness(img_file)
    factor = 0.97
    img_file = enhancer.enhance(factor)
    print(img_file)
    
    sharpener = ImageEnhance.Sharpness(img_file)
    factor = 10
    sharpener.enhance(factor)
    print(img_file)

    img_file.filter(ImageFilter.UnsharpMask(radius=2, percent=150))
    print(img_file)

    return img_file

#img_same regulates whether pictures with one color are sshown in the output or not
def manipulate_created_image(img_file, image_same=True):
    #check if the colors in the picture are all the same
    #st.write("image_same: "+str(image_same))
    with open("C:\\Users\\Ella\\Ella-Kopie\\Studium\\Semester9\\Job\\Mondrian extension for CSV Visualization\\mondrian\\colors.json", "r") as jsonfile:
        data = json.load(jsonfile) # Reading the file
        #print("Read successful")
        jsonfile.close()
    #this loop postulates that if there a color in the image file that is different to the first color,
    #there are >2 colors in the image -> the image has >1 colors
    #print(img_file)

    #st.write(img_file)
    img_colors_all_same = False
    if image_same:
        img_colors_all_same = check_if_image_same(img_file)
        # img_colors_all_same = True
        # #first_list = img_file[0]
        # first_element = img_file[0][0]
        # for list in img_file:
        #     #first_element = list[0]
        #     for element in list:
        #         if first_element != element:
        #             img_colors_all_same = False  
        #     # if list != first_list:
        #     #     img_colors_all_same = False

    img = np.array(img_file,dtype=np.int8)
    img_file = Image.fromarray(img, 'RGB')
    img_file = img_file.resize((data['height'], data['width']), resample=Image.NEAREST)
    enhancer = ImageEnhance.Brightness(img_file)
    factor = 0.97
    img_file = enhancer.enhance(factor)

    return img_colors_all_same,img_file

def check_if_image_same(img_file):
    img_colors_all_same = True
    #first_list = img_file[0]
    st.write(len(img_file))
    #st.write(img_file)
    # if img_file[0]=="":#& len(img_file)==1:
    # #     return img_colors_all_same
    # if os.stat(img_file).st_size == 0:
    #     return img_colors_all_same
    if len(img_file)==0:
        return img_colors_all_same
    first_element = img_file[0][0]
    for list in img_file:
        #first_element = list[0]
        for element in list:
            if first_element != element:
                img_colors_all_same = False  
    # if list != first_list:
    #     img_colors_all_same = False
    return img_colors_all_same


def create_image(table_file_path, separator=None, quotechar=None, escapechar=None , color=False, cell_length=False, **formatparams):
    img1 = table_as_image_better(table_file_path, separator, quotechar, escapechar, color, cell_length, **formatparams)
    img = np.array(img1,dtype= np.int8)
    img_file = Image.fromarray(img, 'RGB')
    img_file = img_file.resize((200, 200), resample=Image.NEAREST)
    enhancer = ImageEnhance.Brightness(img_file)
    factor = 0.97
    img_file = enhancer.enhance(factor)

    return img_file

def create_image_clevercsv(table_file_path, dialect= 'excel', color=False, cell_length=False, **formatparams):
    dialect = dialect_detection_clevercsv(table_file_path)
    img1 = table_as_image_better(table_file_path, dialect, color, cell_length, **formatparams)
    img = np.array(img1,dtype= np.int8)
    img_file = Image.fromarray(img, 'RGB')
    img_file = img_file.resize((200, 200), resample=Image.NEAREST)
    enhancer = ImageEnhance.Brightness(img_file)
    factor = 0.97
    img_file = enhancer.enhance(factor)

    return img_file

def dialect_detection_clevercsv(table_file_path):
    dialect = clevercsv.detect_dialect(table_file_path)

    table_file_path = table_file_path.rsplit('.')[0]
    try:
        #csv.register_dialect("dialect_"+  table_file_path.rsplit('.')[0], delimiter = dialect.delimiter,quotechar=dialect.quotechar, escapechar = dialect.escapechar)
        csv.register_dialect("dialect_"+  table_file_path.rsplit('\\')[len(table_file_path.rsplit('\\'))-1], delimiter = dialect.delimiter,quotechar=dialect.quotechar, escapechar = dialect.escapechar)
    except TypeError:
        csv.register_dialect("dialect_"+ table_file_path.rsplit('\\')[len(table_file_path.rsplit('\\'))-1], delimiter = dialect.delimiter,quotechar='"', escapechar = dialect.escapechar)        
    
    print("dialect_"+ table_file_path.rsplit('\\')[len(table_file_path.rsplit('\\'))-1])
    return "dialect_"+ table_file_path.rsplit('\\')[len(table_file_path.rsplit('\\'))-1]
