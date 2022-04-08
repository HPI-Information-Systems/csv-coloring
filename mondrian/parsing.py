import datetime

import json
import streamlit as st
import matplotlib.colors as colors
import colour
import dateutil.parser
import re
import sys
sys.path.append('C:\\Users\\Ella\\Ella-Kopie\\Studium\\Semester9\\Job\\Mondrian extension for CSV Visualization\\mondrian')

class customDateParserInfo(dateutil.parser.parserinfo):
    JUMP = [' ', '.', ',', ';', '-', '/', "'"]


#differentiate_all_uppercase, differentiate_all_lowercase and differentiate_all_titles, if true, 
# mean that you want the following data to be uniquely coloured by the algorithm
#1. differentiate_all_uppercase: words that only contain uppercase letters + plus non-letter signs
#2. differentiate_all_lowercase: words that only contain lowercase letters + plus non-letter signs
#3. differentiate_all_titles: strings where every word starts with an uppercase letter

def parse_cell(val, color=False):

    with open("C:\\Users\\Ella\\Ella-Kopie\\Studium\\Semester9\\Job\\Mondrian extension for CSV Visualization\\mondrian\\colors.json", "r") as jsonfile:
        data = json.load(jsonfile) # Reading the file
        jsonfile.close()

    #colors that field white if it is a space or if there is nothing in the value that can be split
    #into its parts which means there is nothing in the value and the value is not a space
    if not val.split() or val.isspace():
        return colour.Color(data['EMPTY']).rgb

    if not color:
        return colour.Color(data['NON-EMPTY']).rgb

    comma_split = val.split(",")

    if any([len(x) == 3 for x in comma_split]) and not any([x.isalpha() for x in val]):
        val = re.sub(",", "", val)

    #if val is a non-integer number with numbers before + after comma
    elif len(comma_split) == 2 and not any([x.isalpha() for x in val]):
        val = re.sub(",", ".", val)

    val = val.lstrip().rstrip()

    try:
        int(val)
        return colour.Color(data['INTEGER']).rgb
    except ValueError:
        pass
    try:
        float(val)
        return colour.Color(data['FLOAT']).rgb
    except ValueError:
        pass
    if str(data['differentiate_times'])=="True":
        try:
            datetime.time.fromisoformat(val)
            return colour.Color(data['TIME']).rgb
        except ValueError:
            pass
    if str(data['differentiate_dates'])=="True":
        try:
            dateutil.parser.parse(val, parserinfo=customDateParserInfo())
            return colour.Color(data['DATE']).rgb

        except ValueError:
            pass
        except TypeError:
            pass
            
        #This prevents the error message 'OverflowError: Python int too large to convert to C long'
        except OverflowError:
            pass


    if val.isupper() & (str(data['differentiate_all_uppercase'])=="True"):
        return colour.Color(data['STRING_UPPER']).rgb
    elif val.islower() & (str(data['differentiate_all_lowercase'])=="True"):
        return colour.Color(data['STRING_LOWER']).rgb
    elif val.istitle() & (str(data['differentiate_all_titles'])=="True"):
        return colour.Color(data['STRING_TITLE']).rgb

    return colour.Color(data['STRING_GENERIC']).rgb
