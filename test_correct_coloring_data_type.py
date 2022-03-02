import sys
sys.path.append('C:\\Users\\Ella\\Ella-Kopie\\Studium\\Semester9\\Job\\Mondrian extension for CSV Visualization\\mondrian')
from mondrian.visualization import manipulate_created_image, create_image, table_as_image_better,manipulate_created_image
import pandas as pd
import json
import colour

def test_correct_coloring_data_type():
    with open("mondrian\\colors.json", "r") as jsonfile:
        data = json.load(jsonfile) # Reading the file
        print("Read successful")
        jsonfile.close()
    string_color = '#90ee90'
    int_color = '#ffb6c1'
    float_color = '#add8e6'

    data['STRING_GENERIC']= string_color
    data['INTEGER']= int_color
    data['FLOAT']=  float_color 
            
    lowercase_color ='#32cd32'
    data['STRING_LOWER']=  lowercase_color 
    data['differentiate_all_uppercase'] = "True"

    uppercase_color = '#00ff00'
    data['STRING_UPPER']=  uppercase_color 
    data['differentiate_all_uppercase'] = "True"

    title_color = '#00ff7f'
    data['STRING_TITLE']=  title_color 
    data['differentiate_alle_titles'] = "True"

    with open("mondrian\\colors.json", "w") as jsonfile:
        myJSON = json.dump(data, jsonfile) # Writing to the file
        #print("Write successful")
        jsonfile.close()

    df = pd.read_csv('C:\Users\Ella\Ella-Kopie\Studium\Semester9\Job\Mondrian extension for CSV Visualization\all_data_types.csv')
    test_img = table_as_image_better(df)
    print(test_img)
    correct_result= [colour.Color(data['Integer']).rgb, colour.Color(data['String']).rgb, colour.Color(data['STRING_TITLE'
    ,colour.Color(data['STRING_UPPER']).rgb, colour.Color(data['STRING_LOWER']).rgb,]).rgb,colour.Color(data['DATE']).rgb
    , colour.Color(data['FLOAT']).rgb, colour.Color(data['TIME']).rgb,colour.Color(data['Integer']).rgb, colour.Color(data['String']).rgb, colour.Color(data['STRING_TITLE'
    ,colour.Color(data['STRING_UPPER']).rgb, colour.Color(data['STRING_LOWER']).rgb,]).rgb,colour.Color(data['DATE']).rgb
    , colour.Color(data['FLOAT']).rgb, colour.Color(data['TIME']).rgb]
    assert test_img == correct_result