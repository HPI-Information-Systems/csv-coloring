#from types import CellType
from numpy import string_
import streamlit as st
import json
import pandas as pd
import sys

from streamlit.elements.utils import check_callback_rules
sys.path.append('C:\\Users\\Ella\\Ella-Kopie\\Studium\\Semester9\\Job\\Mondrian extension for CSV Visualization\\mondrian')
from mondrian.visualization import manipulate_created_image, create_image, table_as_image_better,manipulate_created_image
import os
import easygui
import csv
from PIL import ImageColor
import colour

#TODO: Überlege dir, ob du die Farben intern im Hex-oder im RGB-Format speichern möchtest

#i have added the empty string  at the start
special_characters = ['!', '"', '$', '#', '%', '&', '\'', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~','','\\r\\n']

def open_file():
    try:
        file_path = easygui.fileopenbox('Upload your CSV File')
        if file_path is not None:
            print(file_path)
            pass
    except Exception as e:
        print("Error: "+str(e))


#rows are probably the rows that are supposed to be loaded
#sep is the separator
def load_data(uploaded_file, nrows, sep, quotechar = '"', escapechar=None):                                          #  load data from csv file
#def load_data(uploaded_file, nrows, sep):                                          #  load data from csv file#
    #data = pd.read_csv(uploaded_file, sep=sep, nrows=nrows, header=None, quotechar =quotechar, escapechar=escapechar)           #  read csv file
    data = pd.read_csv(uploaded_file, sep=sep, nrows=nrows, quotechar =quotechar, escapechar=escapechar)           #  read csv file
    return data

#collect chosen dialect signs in data file + use them for the loops here
def go_over_characters(file_path, height, width, character_choices, image_same):
    #st.write("Go over characters")
    cols = st.columns(3)
    num = 0
    #st.write("Go over characters")

    separators = character_choices[0]
    quotechars = character_choices[1]
    escapechars = character_choices[2]
    #st.write("Go over characters")

    #added repr into st.write so that \\r\\n will bee displyed properly
    for i in range(0, len(separators)):                     # create image grid
        #st.write("i: "+str(i))                    # create image grid                                
        #st.write('start image loop')
        #st.write(special_characters[separators[i]]) 
        for j in range(0, len(quotechars)): 
            #st.write("j: "+str(j))                    # create image grid 
            #st.write(special_characters[quotechars[j]]) 
            #st.write(len(escapechars))
            for g in range(0, len(escapechars)):
                #st.write("g: "+str(g))                    # create image grid                                
                if num % 3 == 0:
                    if special_characters[g] == '#':
                        #cols[0].subheader("#ㅤ")
                        cols[0].write('separator: '+ f'{special_characters[separators[i]]}' + ', quotechar: ' + f'{special_characters[quotechars[j]]}'+', escapechar: #')
                    else:
                        image_all_same_color, image = manipulate_created_image(table_as_image_better(file_path, delimiter=f'{special_characters[separators[i]]}', quotechar=f'{special_characters[quotechars[j]]}', escapechar=f'{special_characters[g]}'),height, width, image_same)
                        if image_all_same_color:
                            continue
                        cols[0].write('separator: '+ f'{special_characters[separators[i]]}' + ', quotechar: ' + f'{special_characters[quotechars[j]]}'+', escapechar: '+ f'{special_characters[escapechars[g]]}')
                        cols[0].image(image)                
                elif num % 3 == 1:
                    image_all_same_color, image = manipulate_created_image(table_as_image_better(file_path, delimiter=f'{special_characters[separators[i]]}', quotechar=f'{special_characters[quotechars[j]]}', escapechar=f'{special_characters[g]}'),height, width, image_same)
                    if image_all_same_color:
                        continue
                    cols[1].write('separator: '+ f'{special_characters[separators[i]]}' + ', quotechar: ' + f'{special_characters[quotechars[j]]}'+', escapechar: '+ f'{special_characters[escapechars[g]]}')
                    cols[1].image(image)       
                elif num % 3 == 2:
                    image_all_same_color, image = manipulate_created_image(table_as_image_better(file_path, delimiter=f'{special_characters[separators[i]]}', quotechar=f'{special_characters[quotechars[j]]}', escapechar=f'{special_characters[g]}'),height, width, image_same)
                    if image_all_same_color:
                        continue
                    cols[2].write('separator: '+ f'{special_characters[separators[i]]}' + ', quotechar: ' + f'{special_characters[quotechars[j]]}'+', escapechar: '+ f'{special_characters[escapechars[g]]}')
                    cols[2].image(image)    
                num=num+1
                #st.write(num)

def reset_columns_and_rows():
    with open("mondrian\\colors.json", "r") as jsonfile:
        data = json.load(jsonfile) # Reading the file
        print("Read successful")
        jsonfile.close()
    
    data['row_output_from']=0
    data['row_output_until']=0
    data['row_output_start']=0
    data['row_output_end']=0

    data['column_output_from']=0
    data['column_output_until']=0
    data['column_output_start']=0
    data['column_output_end']=0

    with open("mondrian\\colors.json", "w") as jsonfile:
        myJSON = json.dump(data, jsonfile) # Writing to the file
        #print("Write successful")
        jsonfile.close()
           

def highlight_cell(cell_value, int_color, float_color, string_color):
    highlightNone = 'background-color: lightgrey;'                  #  empty cell color
    highlightInt = 'background-color: ' + int_color + ';'           #  integer cell color       
    highlightFloat = 'background-color: ' + float_color + ';'       #  float cell color
    highlightString = 'background-color: ' + string_color + ';'     #  string cell color

    if str(cell_value) == 'nan':                                    #  if cell is empty
        return highlightNone
    else:
        try:
            int(str(cell_value))                                    #  if cell is integer
            return highlightInt
        except:
            try:
                float(str(cell_value))                              #  if cell is float
                return highlightFloat
            except:
                return highlightString                               #  if cell is string
    
    return highlightString


def check_path(file_path):
    if os.path.isfile(file_path):
        return True
    else:
        return False

def append_existing_file(uploaded_sep_file, uploaded_file, sep):
    new_row = pd.DataFrame({'file_name': [uploaded_file],'seperator': [sep]})
    df = pd.read_csv(uploaded_sep_file, sep=',', error_bad_lines=False)
    new_row.to_csv(f'{df}', mode='a', header=False,)
    return df

def set_characters():
            st.subheader('Select a delimiter (You must select at least one)')
            cols = st.columns(9)

            extraspecial_chars = list(special_characters)
            choose_delimiter=[]
            delimiter_indices=[]
            choose_all= st.checkbox('Choose all characters', key=7)
            # am excluding the characters that get rejected by the reader from what is shown,
            # may have to change code to accomodate them
            for i in range(0, len(extraspecial_chars)):
                if choose_all:
                    if extraspecial_chars[i]==',': 
                        delimiter_choice=cols[i%9].checkbox(',',True, key=10)
                    elif extraspecial_chars[i]=='': 
                        delimiter_choice=False
                        pass
                    elif extraspecial_chars[i]=="\\r\\n":
                        delimiter_choice=False
                        pass
                    else:
                        delimiter_choice=cols[i%9].checkbox(extraspecial_chars[i],True, key=10)
                elif extraspecial_chars[i]==',': 
                    delimiter_choice=cols[i%9].checkbox(',',True, key=10)
                elif extraspecial_chars[i]=="\\r\\n":
                    delimiter_choice=False
                    #pass
                elif extraspecial_chars[i]=='':
                    delimiter_choice=False
                    pass
                else: 
                    delimiter_choice=cols[i%9].checkbox(extraspecial_chars[i], key=10)
                choose_delimiter.append(delimiter_choice)
                if delimiter_choice:
                    delimiter_indices.append(i)

            
            st.subheader('Select a quotechar (You must choose at least one)')
            cols = st.columns(9)
            choose_quotechars=[]
            quotechar_indices=[]
            choose_all= st.checkbox('Choose all characters', key=8)
            for i in range(0, len(extraspecial_chars)):
                if choose_all:
                    if extraspecial_chars[i]=='"': 
                        quotechar_choice=cols[i%9].checkbox('"',True, key=11)
                    elif extraspecial_chars[i]=='': 
                        quotechar_choice=cols[i%9].checkbox('"',True, key=11)
                    else:
                        quotechar_choice=cols[i%9].checkbox(extraspecial_chars[i],True, key=11)
                elif extraspecial_chars[i]=='': 
                    pass
                elif extraspecial_chars[i]=='"': 
                    quotechar_choice=cols[i%9].checkbox('"',True, key=11)
                elif extraspecial_chars[i]=='':
                    quotechar_choice=cols[i%9].checkbox('',True, key=11)
                else: 
                    quotechar_choice=cols[i%9].checkbox(extraspecial_chars[i], key=11)     
                choose_quotechars.append(quotechar_choice)
                if quotechar_choice:
                    quotechar_indices.append(i)
            
            st.subheader('Select the right escapechar')
            cols = st.columns(9)
            choose_escapechars=[]
            escapechar_indices=[]
            choose_all= st.checkbox('Choose all characters', key=9)
            for i in range(0, len(extraspecial_chars)):
                if choose_all:
                    if extraspecial_chars[i]=='\\r\\n':
                        escapechar_choice=cols[i%9].checkbox('\\r\\n',True, key=12)
                    else:    
                        escapechar_choice=cols[i%9].checkbox(extraspecial_chars[i],True, key=12)
                elif extraspecial_chars[i]=='\\r\\n':
                    escapechar_choice=cols[i%9].checkbox('\\r\\n',True, key=12)
                else: 
                    escapechar_choice=cols[i%9].checkbox(extraspecial_chars[i], key=12)                
                choose_escapechars.append(escapechar_choice)
                if escapechar_choice:
                    escapechar_indices.append(i)

            character_choices=[]
            character_choices.append(delimiter_indices)
            character_choices.append(quotechar_indices)
            character_choices.append(escapechar_indices)

            return character_choices

def set_colors():
            with open("mondrian\\colors.json", "r") as jsonfile:
                data = json.load(jsonfile) # Reading the file
                print("Read successful")
                jsonfile.close()
            st.sidebar.subheader('Select the colors for the data types')
            cols = st.sidebar.columns(3)      
            string_color = cols[0].color_picker(                            #  set string color
                'String color', 
                value='#90ee90'
            )     
            int_color = cols[1].color_picker(                               #  set int color
            'Integer color', 
            value='#ffb6c1'
            )           
            float_color = cols[2].color_picker(                             #  set float color
            'Float color', 
            value='#add8e6'
            )  

            check_lowercase_strings = st.checkbox('Show all-lowercase strings in their own color')
            check_uppercase_strings = st.checkbox('Show all-uppercase strings in their own color')
            check_title_strings = st.checkbox('Show title strings(at the beginning of each word is a capital letter  and nowhere else) in their own color')

            data['STRING_GENERIC']= string_color
            data['INTEGER']= int_color
            data['FLOAT']=  float_color 
            
            if check_lowercase_strings:
                lowercase_color = cols[0].color_picker(                             #  set float color
                    'Lowercase string color', 
                    value='#32cd32'
                )  
                data['STRING_LOWER']=  lowercase_color 
                data['differentiate_all_uppercase'] = "True"

            if check_uppercase_strings:
                uppercase_color = cols[1].color_picker(                             #  set float color
                    'Uppercase string color', 
                    value='#00ff00'
                )  
                data['STRING_UPPER']=  uppercase_color 
                data['differentiate_all_uppercase'] = "True"


            if check_title_strings:    
                title_color = cols[2].color_picker(                             #  set float color
                    'Title string color', 
                    value='#00ff7f'
                )        
                data['STRING_TITLE']=  title_color 
                data['differentiate_alle_titles'] = "True"

            with open("mondrian\\colors.json", "w") as jsonfile:
                myJSON = json.dump(data, jsonfile) # Writing to the file
                #print("Write successful")
                jsonfile.close()

def set_row_settings():

            with open("mondrian\\colors.json", "r") as jsonfile:
                data = json.load(jsonfile) # Reading the file
                print("Read successful")
                jsonfile.close()
            display_all_rows_in_file = "Display the color for alle lines in the csv file"
            row_output_start = 'Display first ... lines'
            row_output_end = 'Display last ... lines'
            start_to_stop_rows = 'Display image from line ... to line ...'

            row_settings = [row_output_start, row_output_end, start_to_stop_rows, display_all_rows_in_file]
            row_settings_radio = st.radio('Change the way the rows of the csv file are displayed',row_settings)
            #you somehow need to make it so that the first 2 options do not exclude each other
            #idea: trigger condition even if only  one of them is picked - but you schould be able to pick 
            #two at the sametime!?
            if row_settings_radio == start_to_stop_rows:
                #TODO: make it so that both picking or not picking the other value produces a result
                # where both values get a value
                start_row = st.number_input('Display from the ...th row on', 0)
            #if line_settings_radio== line_output_at_stop:
                stop_row = st.number_input('Display up unto ...th row',0)
                if start_row> stop_row:
                    st.write('The row where the output starts comes later than the one where the output stops. In this case the program will ouput the'
                    +'the image with all row. Please change the values accordingly if you do not want that.')
                elif start_row == stop_row:
                    st.write('The row where the output starts must not be equal to the one where the output stops. In this case the program will ouput the'
                    +'the image with all rows. Please change the values accordingly if you do not want that.')
                else:
                    data['row_output_from']=start_row
                    data['row_output_until']=stop_row
            #just making this dependent on first if is not good -> TODO: fix this!
            elif  row_settings_radio ==row_output_start:
                number_start_rows = st.number_input('Display first  ... rows',0)
                data['row_output_start']=number_start_rows
            elif  row_settings_radio ==row_output_end:
                number_end_rows = st.number_input('Display last ... rows',0)
                data['row_output_end']=number_end_rows
            st.write("If any other options than 'display all lines in file' is chosen but all input numbers "
            +"are 0, then the execution will be as if 'display all lines in file' had been chosen")
            with open("mondrian\\colors.json", "w") as jsonfile:
                myJSON = json.dump(data, jsonfile) # Writing to the file
                #print("Write successful")
                jsonfile.close()

def set_column_settings():

            with open("mondrian\\colors.json", "r") as jsonfile:
                data = json.load(jsonfile) # Reading the file
                print("Read successful")
                jsonfile.close()
            display_all_columns_in_file = "Display the color for all columns in the csv file"
            column_output_start = 'Display first ... columns'
            column_output_end = 'Display last ... column'
            start_to_stop_columns = 'Display image from column ... to column ...'
            

            column_settings = [column_output_start, column_output_end, start_to_stop_columns, display_all_columns_in_file]
            column_settings_radio = st.radio('Change the way the columns of the csv file are displayed', column_settings)
            #you somehow need to make it so that the first 2 options do not exclude each other
            #idea: trigger condition even if only  one of them is picked - but you schould be able to pick 
            #two at the sametime!?
            if column_settings_radio == start_to_stop_columns:
                reset_columns_and_rows()
                #TODO: make it so that both picking or not picking the other value produces a result
                # where both values get a value
                start_column = st.number_input('Display from the ...th column on', 0)
            #if line_settings_radio== line_output_at_stop:
                stop_column = st.number_input('Display up unto ... lines',0)
                if start_column> stop_column:
                    st.write('The column where the output starts comes later than the one where the output stops. In this case the program will ouput the'
                    +'the image with all columns. Please change the values accordingly if you do not want that.')
                elif start_column == stop_column:
                    st.write('The column where the output starts must not be equal to the one where the output stops. In this case the program will ouput the'
                    +'the image with all columns. Please change the values accordingly if you do not want that.')
                else:
                    data['column_output_from']=start_column
                    data['column_output_until']=stop_column
            #just making this dependent on first if is not good -> TODO: fix this!
            elif  column_settings_radio ==column_output_start:
                reset_columns_and_rows()
                number_start_columns = st.number_input('Display first  ... columns',0)
                data['column_output_start']=number_start_columns
            elif  column_settings_radio ==column_output_end:
                reset_columns_and_rows()
                number_end_columns = st.number_input('Display last ... columns',0)
                data['column_output_end']=number_end_columns
            st.write("If any other options than 'display all column in file' is chosen but all input numbers "+
            "are 0, then the execution will be as if 'display all columns in file' had been chosen")
            with open("mondrian\\colors.json", "w") as jsonfile:
                myJSON = json.dump(data, jsonfile) # Writing to the file
                #print("Write successful")
                jsonfile.close()

def set_height_and_width():
            with open("mondrian\\colors.json", "r") as jsonfile:
                data = json.load(jsonfile) # Reading the file
                print("Read successful")
                jsonfile.close()
            height = st.number_input('Height of generated picture',200)
            data['height']= height
            width = st.number_input('Width of generated picture', 200)
            data['width'] = width
            with open("mondrian\\colors.json", "w") as jsonfile:
                myJSON = json.dump(data, jsonfile) # Writing to the file
                #print("Write successful")
                jsonfile.close()

def app():
    st.sidebar.title('Select a tool')
    page = st.sidebar.radio('', ('CSV Annotation check', 'CSV Dialect detection'))
    st.title(page)
    st.sidebar.markdown(f'# {page}')
    file_path = st.sidebar.text_input('Enter the path to your CSV File')
    st.sidebar.subheader('Your CSV file:')
    if not file_path: #TODO: Check if String is file path
        st.sidebar.markdown('No file uploaded/Invalid path')
    elif not file_path.endswith('.csv'):
        st.sidebar.markdown('This is not a CSV file')
    else:
        st.sidebar.markdown(os.path.basename(file_path))
        if page == 'CSV Annotation check':
            st.sidebar.subheader('CSV Settings')
            rowsToShow = st.sidebar.number_input(                           #  set number of rows to show
                'How many rows do you want to show?',             
                min_value=1,                                                #  minimum value
                value=20                                                    #  default value
            ) 
            selected_separator = st.sidebar.text_input(               #  set seperator
                'Enter the seperator you want to test.', 
                ','                                                         #  default seperator
            )
            selected_quoting_type = st.sidebar.text_input(               #  set seperator
                'Enter the quote character you want to test.', 
                '"'                                                         #  default seperator
            )
            selected_seperating_type = st.sidebar.text_input(               #  set seperator
                'Enter the escape character you want to test.', 
                '\n'                                                         #  default seperator
            )
            st.sidebar.subheader('Select the colors for the data types')
            cols = st.sidebar.columns(3)                                            
            string_color = cols[0].color_picker(                            #  set string color
                'String color', 
                value='#90ee90'
            )     
            int_color = cols[1].color_picker(                               #  set int color
            'Integer color', 
            value='#ffb6c1'
            )           
            float_color = cols[2].color_picker(                             #  set float color
            'Float color', 
            value='#add8e6'
            )                       
            data = load_data(file_path,sep=selected_separator, nrows=rowsToShow, quotechar=selected_quoting_type, escapechar= selected_seperating_type)
            st.dataframe(data.style.applymap(lambda x:highlight_cell(x,int_color, float_color, string_color )))               #  display data in table with highlighted cells
        elif page == 'CSV Dialect detection':
            # st.sidebar.subheader('Remember the chosen seperator')
            # already_seperator_file = st.sidebar.checkbox('I already have a file with seperators for files')
            # st.write('<style>div.row-widget.stRadio>div{flex-direction:row;grid-column-gap:30px;}</style>', unsafe_allow_html=True) #Set alignment of radio buttons
            # choose=st.radio("Select the right seperator",(special_characters))
            
            st.sidebar.subheader('Remember the chosen delimiter')
            already_seperator_file = st.sidebar.checkbox('I already have a file with delimiters for files')
            st.write('<style>div.row-widget.stRadio>div{flex-direction:row;grid-column-gap:30px;}</style>', unsafe_allow_html=True) #Set alignment of radio buttons
            extraspecial_chars = list(special_characters)

            st.subheader('Select a delimiter (You must select at least one)')
            cols = st.columns(9)

            character_choices = set_characters()
            #st.write(character_choices)

            # with open("mondrian\\colors.json", "r") as jsonfile:
            #     data = json.load(jsonfile) # Reading the file
            #     print("Read successful")
            #     jsonfile.close()
            # height = st.number_input('Height of generated picture',200)
            # data['height']= height
            # width = st.number_input('Width of generated picture', 200)
            # data['width'] = width

            # display_all_rows_in_file = "Display the color for alle lines in the csv file"
            # row_output_start = 'Display first ... lines'
            # row_output_end = 'Display last ... lines'
            # start_to_stop_rows = 'Display image from line ... to line ...'

            # row_settings = [row_output_start, row_output_end, start_to_stop_rows, display_all_rows_in_file]
            # row_settings_radio = st.radio('Change the way the rows of the csv file are displayed',row_settings)
            # #you somehow need to make it so that the first 2 options do not exclude each other
            # #idea: trigger condition even if only  one of them is picked - but you schould be able to pick 
            # #two at the sametime!?
            # if row_settings_radio == start_to_stop_rows:
            #     #TODO: make it so that both picking or not picking the other value produces a result
            #     # where both values get a value
            #     start_row = st.number_input('Display from the ...th row on', 0)
            # #if line_settings_radio== line_output_at_stop:
            #     stop_row = st.number_input('Display up unto ...th row',0)
            #     if start_row> stop_row:
            #         st.write('The row where the output starts comes later than the one where the output stops. In this case the program will ouput the'
            #         +'the image with all row. Please change the values accordingly if you do not want that.')
            #     elif start_row == stop_row:
            #         st.write('The row where the output starts must not be equal to the one where the output stops. In this case the program will ouput the'
            #         +'the image with all rows. Please change the values accordingly if you do not want that.')
            #     else:
            #         data['row_output_from']=start_row
            #         data['row_output_until']=stop_row
            # #just making this dependent on first if is not good -> TODO: fix this!
            # elif  row_settings_radio ==row_output_start:
            #     number_start_rows = st.number_input('Display first  ... rows',0)
            #     data['row_output_start']=number_start_rows
            # elif  row_settings_radio ==row_output_end:
            #     number_end_rows = st.number_input('Display last ... rows',0)
            #     data['row_output_end']=number_end_rows
            # st.write("If any other options than 'display all lines in file' is chosen but all input numbers "+
            # "are 0, then the execution will be as if 'display all lines in file' had been chosen")
            # #do you need to do anything in the else case - > no, because then everything else is 
            # #displayed anyway

            # display_all_columns_in_file = "Display the color for all columns in the csv file"
            # column_output_start = 'Display first ... columns'
            # column_output_end = 'Display last ... column'
            # start_to_stop_columns = 'Display image from column ... to column ...'
            

            # column_settings = [column_output_start, column_output_end, start_to_stop_columns, display_all_columns_in_file]
            # column_settings_radio = st.radio('Change the way the columns of the csv file are displayed', column_settings)
            # #you somehow need to make it so that the first 2 options do not exclude each other
            # #idea: trigger condition even if only  one of them is picked - but you schould be able to pick 
            # #two at the sametime!?
            # if column_settings_radio == start_to_stop_columns:
            #     reset_columns_and_rows()
            #     #TODO: make it so that both picking or not picking the other value produces a result
            #     # where both values get a value
            #     start_column = st.number_input('Display from the ...th column on', 0)
            # #if line_settings_radio== line_output_at_stop:
            #     stop_column = st.number_input('Display up unto ... lines',0)
            #     if start_column> stop_column:
            #         st.write('The column where the output starts comes later than the one where the output stops. In this case the program will ouput the'
            #         +'the image with all columns. Please change the values accordingly if you do not want that.')
            #     elif start_column == stop_column:
            #         st.write('The column where the output starts must not be equal to the one where the output stops. In this case the program will ouput the'
            #         +'the image with all columns. Please change the values accordingly if you do not want that.')
            #     else:
            #         data['column_output_from']=start_column
            #         data['column_output_until']=stop_column
            # #just making this dependent on first if is not good -> TODO: fix this!
            # elif  column_settings_radio ==column_output_start:
            #     reset_columns_and_rows()
            #     number_start_columns = st.number_input('Display first  ... columns',0)
            #     data['column_output_start']=number_start_columns
            # elif  column_settings_radio ==column_output_end:
            #     reset_columns_and_rows()
            #     number_end_columns = st.number_input('Display last ... columns',0)
            #     data['column_output_end']=number_end_columns
            # st.write("If any other options than 'display all column in file' is chosen but all input numbers "+
            # "are 0, then the execution will be as if 'display all columns in file' had been chosen")
            set_height_and_width()
            set_row_settings()
            set_column_settings()
            #right now pretty much all preset values are 0 -> these values mean that nothing needs to be
            #changed because once you activated the visualization we  are certain you want to see an image            #idea: once something has been chosen, automatically write it into the config file
            #this also means that you need default settings for them 
            #why do you add different data blocks to json files, bc right now my file has everything
            #in the same data
            st.write("Please note that depending on the used dialect, there may not be as many lines in the file as are given above so we will choose an approximate amount of the total lines")
        
            set_colors()

            # with open("mondrian\\colors.json", "w") as jsonfile:
            #     myJSON = json.dump(data, jsonfile) # Writing to the file
            #     #print("Write successful")
            #     jsonfile.close()

            image_same= st.checkbox('Do not show results with one color/one recognized data type', True)
            button = st.button('Create visualization')
            if button:
                    st.write('Starting Loop')
                    go_over_characters(file_path, width, height, character_choices,image_same)
                    #this part is for selecting the quotechar
            else:
                st.write('You have not pressed the button yet.')
            if already_seperator_file:
                    st.sidebar.markdown('<p style ="color: red; font-weight: bold">!!! The file needs to have a format like this:', unsafe_allow_html=True)
                    st.sidebar.table(pd.DataFrame({'file_name': ['google_yearly_income.csv', 'amazon_yearly_income.csv', 'facebook_yearly_income.csv'],'seperator': [',', ';', '|']}))
                    uploaded_seperator_file = st.sidebar.file_uploader('Upload your seperator file', type=['csv'])
                    if uploaded_seperator_file is None:
                        st.sidebar.markdown('No file uploaded')
                    else:
                        st.sidebar.markdown(f'File name: {uploaded_seperator_file.name}')
                        
                        #TODO: Fix adding line to file
                        #st.sidebar.download_button('Download file with added line', file_name=f'{uploaded_seperator_file.name}',data=append_existing_file(uploaded_seperator_file, file_path, '"' + choose_sep + '"')),
                        st.sidebar.download_button('Download file with added line', file_name=f'{uploaded_seperator_file.name}',data=append_existing_file(uploaded_seperator_file, file_path, '"' + ',' + '"')),
            else:
                #st.sidebar.download_button('Generate a file for me and download it', file_name='seperator_file.csv', data=pd.DataFrame({'file_name': [file_path],'seperator': ['"' + choose_sep + '"']}).to_csv(sep=','))
                st.sidebar.download_button('Generate a file for me and download it', file_name='seperator_file.csv', data=pd.DataFrame({'file_name': [file_path],'seperator': ['"' + ',' + '"']}).to_csv(sep=','))    
    
