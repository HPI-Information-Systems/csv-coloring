#from types import CellType
import streamlit as st
import json
import pandas as pd
import sys
import math

sys.path.append('C:\\Users\\Ella\\Ella-Kopie\\Studium\\Semester9\\Job\\Mondrian extension for CSV Visualization\\mondrian')
from mondrian.visualization import manipulate_created_image, table_as_image_better,manipulate_created_image
import os
import easygui

special_characters = ['!', '"', '$', '#', '%', '&', '\'', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~','','\\r\\n']

with open("mondrian\\colors.json", "r") as jsonfile:
        data = json.load(jsonfile) # Reading the file
        jsonfile.close()

def open_file():
    try:
        file_path = easygui.fileopenbox('Upload your CSV File')
        if file_path is not None:
            print(file_path)
            pass
    except Exception as e:
        print("Error: "+str(e))


def load_data(uploaded_file, nrows, sep, quotechar = '"', escapechar=None):                                          #  load data from csv file
    data = pd.read_csv(uploaded_file, sep=sep, nrows=nrows, quotechar =quotechar, escapechar=escapechar)           #  read csv file
    return data

#generates and places images
def go_over_characters(file_path, character_choices, image_same, resampling_indices):
    # this part is for generating the numbers of columns depending on image width
    # i am assuming there are 1000 pixels for columns + image width in pixels
    # this algorithm is mostly chosen because the past results achieved with  it looked good,

    #TODO: improve algorithm to be more methodical, if possible
    with open("mondrian\\colors.json", "r") as jsonfile:
        data = json.load(jsonfile) # Reading the file
        jsonfile.close()

    max_pics_on_page = math.floor(1000/data["width"])
    space_pics_with_gaps = max_pics_on_page*data['width'] + (max_pics_on_page-1)*data["width"]

    #if number of images(max_pics_on_pages) times their width + plus the gaps inbetween
    # times that width is bigger than the 1000 pixel we assume to be all available 
    # space, we reduce the total number of images and check agian
    while (space_pics_with_gaps>1000) & (max_pics_on_page >1):
        max_pics_on_page = max_pics_on_page-1
        space_pics_with_gaps = max_pics_on_page*data['width'] + (max_pics_on_page-1)*data["width"]

    cols = st.columns(3)
    num = 0

    separators = character_choices[0]
    quotechars = character_choices[1]
    escapechars = character_choices[2]

    #generates images depending on the chosen dialect characters    
    for i in range(0, len(separators)):               
        for j in range(0, len(quotechars)): 
            
            for g in range(0, len(escapechars)):
                if num % 3 == 0:
                    if special_characters[g] == '#':
                        cols[num % max_pics_on_page].write('separator: '+ f'{special_characters[separators[i]]}' + ', quotechar: ' + f'{special_characters[quotechars[j]]}'+', escapechar: #')                        
                        num = num+1              

                    else:
                        for resampling_method in resampling_indices:
                            image_all_same_color, image = manipulate_created_image(table_as_image_better(file_path, config_file_data=data, delimiter=f'{special_characters[separators[i]]}', quotechar=f'{special_characters[quotechars[j]]}', escapechar=f'{special_characters[g]}'), image_same, resampling_method)
                            if image_all_same_color:
                                continue
                            cols[num % max_pics_on_page].write('separator: '+ f'{special_characters[separators[i]]}' + ', quotechar: ' + f'{special_characters[quotechars[j]]}'+', escapechar :'+f'{special_characters[g]}')                        
                            cols[num % max_pics_on_page].image(image)    
                            num = num+1              
                elif num % 3 == 1:
                    for resampling_method in resampling_indices:
                        image_all_same_color, image = manipulate_created_image(table_as_image_better(file_path,config_file_data=data, delimiter=f'{special_characters[separators[i]]}', quotechar=f'{special_characters[quotechars[j]]}', escapechar=f'{special_characters[g]}'), image_same,resampling_method)
                        if image_all_same_color:
                            continue
                        cols[num % max_pics_on_page].write('separator: '+ f'{special_characters[separators[i]]}' + ', quotechar: ' + f'{special_characters[quotechars[j]]}'+', escapechar: '+f'{special_characters[g]}')                        
                        cols[num % max_pics_on_page].image(image)    
                        cols[num % 3].image(image)    
                        num=num+1   
                elif num % 3 == 2:
                    for resampling_method in resampling_indices:
                        image_all_same_color, image = manipulate_created_image(table_as_image_better(file_path,config_file_data=data, delimiter=f'{special_characters[separators[i]]}', quotechar=f'{special_characters[quotechars[j]]}', escapechar=f'{special_characters[g]}'), image_same, resampling_method)
                        if image_all_same_color:
                            continue
                        cols[num % max_pics_on_page].write('separator: '+ f'{special_characters[separators[i]]}' + ', quotechar: ' + f'{special_characters[quotechars[j]]}'+', escapechar: '+f'{special_characters[g]}')                        
                        cols[num % max_pics_on_page].image(image)    
                        num=num+1

def reset_columns_and_rows():
    with open("mondrian\\colors.json", "r") as jsonfile:
        data = json.load(jsonfile) # Reading the file
        jsonfile.close()
    
    data['row_output_from']=0
    data['row_output_until']=0
    data['row_output_start']=0
    data['row_output_end']=0

    with open("mondrian\\colors.json", "w") as jsonfile:
        json.dump(data, jsonfile) 
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
    # am excluding the characters that get rejected by the csv reader 
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
                pass
            elif extraspecial_chars[i]=="\\r\\n":
                pass
            else:
                quotechar_choice=cols[i%9].checkbox(extraspecial_chars[i],True, key=19)
        elif extraspecial_chars[i]=='': 
            pass
        elif extraspecial_chars[i]=='"': 
            quotechar_choice=cols[i%9].checkbox('"',True, key=15)
        elif extraspecial_chars[i]=='':
            quotechar_choice=cols[i%9].checkbox('',True, key=16)
        elif extraspecial_chars[i]=="\\r\\n":
            pass
        else: 
            quotechar_choice=cols[i%9].checkbox(extraspecial_chars[i], key=17)     
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
            if extraspecial_chars[i]=='"':
                escapechar_choice=cols[i%9].checkbox('"',True, key=12)
            elif extraspecial_chars[i]=='': 
                escapechar_choice=False
                pass
            elif extraspecial_chars[i]=="\\r\\n":
                delimiter_choice=False
                pass
            else:    
                escapechar_choice=cols[i%9].checkbox(extraspecial_chars[i],True, key=12)
        elif extraspecial_chars[i]=='"':
            escapechar_choice=cols[i%9].checkbox('"',True, key=12)
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


#set colors for data types
def set_colors():
    with open("mondrian\\colors.json", "r") as jsonfile:
        data = json.load(jsonfile) # Reading the file
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
    check_time = st.checkbox('Show times in their own color')
    check_date = st.checkbox('Show dates in their own color')
    check_separator_rows=st.checkbox('Divide rows with black row')

    data['STRING_GENERIC']= string_color
    data['INTEGER']= int_color
    data['FLOAT']=  float_color 


    if check_separator_rows:
        data['separator_rows']= 'True'

    if check_lowercase_strings:
        lowercase_color = cols[0].color_picker(                             
            'Lowercase string color', 
            value='#32cd32'
            )  
        data['STRING_LOWER']=  lowercase_color 
        data['differentiate_all_lowercase'] = "True"

    if check_uppercase_strings:
        uppercase_color = cols[1].color_picker(                             
            'Uppercase string color', 
            value='#00ff00'
            )  
            
        data['STRING_UPPER']=  uppercase_color 
        data['differentiate_all_uppercase'] = "True"

    if check_title_strings:    
        title_color = cols[2].color_picker(                             
            'Title string color', 
            value='#00ff7f'
            )        
        data['STRING_TITLE']=  title_color 
        data['differentiate_all_titles'] = "True"

    if check_date:    
        date_color = cols[2].color_picker(                             
            'Date color', 
            value="#9370db"
            )        
        data['DATE']=  date_color 
        data['differentiate_dates'] = "True"


    if check_time:    
        time_color = cols[2].color_picker(                            
            'Time color', 
                value="#ba55d3"
            )        
        data['TIME']=  time_color 
        data['differentiate_times'] = "True"

    with open("mondrian\\colors.json", "w") as jsonfile:
        json.dump(data, jsonfile) 
        jsonfile.close()

#set which rows are supposed to be displayed
def set_row_settings():

    with open("mondrian\\colors.json", "r") as jsonfile:
        data = json.load(jsonfile) # Reading the file
        jsonfile.close()
    display_all_rows_in_file = "Display the color for all lines in the csv file"
    row_output_start = 'Display first ... lines'
    row_output_end = 'Display last ... lines'
    start_to_stop_rows = 'Display image from line ... to line ...'

    row_settings = [display_all_rows_in_file, row_output_start, row_output_end, start_to_stop_rows]
    row_settings_radio = st.radio('Change the way the rows of the csv file are displayed',row_settings)
            
    if row_settings_radio == start_to_stop_rows:
        #TODO: make it so that both picking or not picking the other value produces a result
        # where both values get a value
        start_row = st.number_input('Display from the ...th row on', 0)
        #if line_settings_radio== line_output_at_stop:
        stop_row = st.number_input('Display up unto ...th row',0)
        if start_row> stop_row:
            st.write('The row where the output starts comes later than the one where the output stops. In this case the program will ouput the'
            +'the image with all rows. Please change the values if that is undesired.')
        elif start_row == stop_row:
            st.write('The row where the output starts must not be equal to the one where the output stops. In this case the program will output '
            +'the image with all rows. Please change the values if you do not want that.')
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
    st.write("Please note that depending on the used dialect, there may not be as many lines in the file as are given above so we will only display the lines within your given space that actually exist in the file")

    with open("mondrian\\colors.json", "w") as jsonfile:
        json.dump(data, jsonfile) # Writing to the file
        jsonfile.close()

#sets resampling algorithm for generated picture
def set_resampling_algorithm():
    with open("mondrian\\colors.json", "r") as jsonfile:
        json.load(jsonfile)
        jsonfile.close()

    st.write('Select a resampling method. Please note that each chosen method will be used on '
    +'every dialect option you chose')
    cols = st.columns(6)
    resampling_settings = ["Nearest-neighbor  Interpolation", "Bilinear algorithm", "Bicubic algorithm", "Box Sampling","Lanczos Resampling", "Hamming algorithm"]

    choose_all= st.checkbox('Choose all characters', key=14)
    # am excluding the characters that get rejected by the csv reader

    resampling_indices=[]
    for i in range(0, len(resampling_settings)):
        if choose_all:
            resampling_choice=cols[i%6].checkbox(resampling_settings[i],True, key=10)
        else: 
            if resampling_settings[i] == "Nearest-neighbor  Interpolation":
                resampling_choice=cols[i%6].checkbox(resampling_settings[i], True, key=10)
            else:
                resampling_choice=cols[i%6].checkbox(resampling_settings[i], key=10)
        if resampling_choice:
            resampling_indices.append(resampling_settings[i])
        
    if len(resampling_indices)<1:
        st.write("Please choose at least one resampling algorithm or there wil be no picture upon"
        +"pressing the button")

    return resampling_indices

#this was supposed to be used with a function that controlled how which columns
#were used in the generated image
#that function was not implemented, it is useless now
def set_column_settings_deprecated():

    with open("mondrian\\colors.json", "r") as jsonfile:
        data = json.load(jsonfile) # Reading the file
        jsonfile.close()

    display_all_columns_in_file = "Display the color for all columns in the csv file"
    column_output_start = 'Display first ... columns'
    column_output_end = 'Display last ... column'
    start_to_stop_columns = 'Display image from column ... to column ...'
            
    column_settings = [ display_all_columns_in_file, column_output_start, column_output_end, start_to_stop_columns]
    column_settings_radio = st.radio('Change the way the columns of the csv file are displayed', column_settings)
    if column_settings_radio == start_to_stop_columns:
        reset_columns_and_rows()

        start_column = st.number_input('Display from the ...th column on', 0)
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
            
    st.write("Please note that depending on the used dialect, there may not be as many lines in the file as are given above so we will only display the lines within your given space that actually exist in the file")

    with open("mondrian\\colors.json", "w") as jsonfile:
        json.dump(data, jsonfile) 
        jsonfile.close()

def set_height_and_width():
    with open("mondrian\\colors.json", "r") as jsonfile:
        data = json.load(jsonfile)
        jsonfile.close()
    height = st.number_input('Height of generated picture',200)
    data['height']= height
    width = st.number_input('Width of generated picture', 200)
    data['width'] = width
    with open("mondrian\\colors.json", "w") as jsonfile:
        json.dump(data, jsonfile) # Writing to the file
        jsonfile.close()
    
#resets the contents of the config file containing the image data back to default
def reset_config_file():
    with open("mondrian\\colors.json", "r") as jsonfile:
        data = json.load(jsonfile) 
        jsonfile.close()
    string_color ='#90ee90'
    int_color ='#ffb6c1'        
    float_color ='#add8e6'

    data['STRING_GENERIC']= string_color
    data['INTEGER']= int_color
    data['FLOAT']=  float_color 
            
    lowercase_color = '#32cd32'
    data['STRING_LOWER']=  lowercase_color 
    data['differentiate_all_uppercase'] = "False"

    uppercase_color = '#00ff00'
    data['STRING_UPPER']=  uppercase_color 
    data['differentiate_all_uppercase'] = "False"

    title_color = '#00ff7f'
    data['STRING_TITLE']=  title_color 
    data['differentiate_alle_titles'] = "False"

    date_color = "#9370db"
    data['DATE']=  date_color 
    data['differentiate_dates'] = "False"

    time_color = "#ba55d3"
    data['TIME']=  time_color 
    data['differentiate_times'] = "False"

    data['separator_rows']= 'False'

    data['row_output_from']= 0
    data['row_output_until']= 0

    with open("mondrian\\colors.json", "w") as jsonfile:
        json.dump(data, jsonfile)
        jsonfile.close()

def app():
    reset_config_file()
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
            
            st.sidebar.subheader('Remember the chosen delimiter')
            already_seperator_file = st.sidebar.checkbox('I already have a file with delimiters for files')
            st.write('<style>div.row-widget.stRadio>div{flex-direction:row;grid-column-gap:30px;}</style>', unsafe_allow_html=True) #Set alignment of radio buttons

            character_choices = set_characters()

            set_height_and_width()
            set_row_settings()
            resampling_indices = set_resampling_algorithm() 

            set_colors()

            image_same= st.checkbox('Do not show results with one color/one recognized data type', True)
           
            button = st.button('Create visualization')
            if button:
                    go_over_characters(file_path, character_choices,image_same, resampling_indices)
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
                        
                        st.sidebar.download_button('Download file with added line', file_name=f'{uploaded_seperator_file.name}',data=append_existing_file(uploaded_seperator_file, file_path, '"' + ',' + '"')),
            else:
                st.sidebar.download_button('Generate a file for me and download it', file_name='seperator_file.csv', data=pd.DataFrame({'file_name': [file_path],'seperator': ['"' + ',' + '"']}).to_csv(sep=','))    
    
