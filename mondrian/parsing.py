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


#differentiate_all_uppercase, differentiate_all_lowercase and differentiate_all_titles, if true, mean that you 
# want
#1. differentiate_all_uppercase: words that only contain uppercase letters + plus non-letter signs
#2. differentiate_all_lowercase: words that only contain lowercase letters + plus non-letter signs
#3. differentiate_all_titles: strings where every word starts with an uppercase letter
# to be differently coloured by the algorithm

#@st.cache(ttl= 24*3600, max_entries= 20) 
def parse_cell(val, color=False):

    with open("C:\\Users\\Ella\\Ella-Kopie\\Studium\\Semester9\\Job\\Mondrian extension for CSV Visualization\\mondrian\\colors.json", "r") as jsonfile:
        data = json.load(jsonfile) # Reading the file
        #print("Read successful")
        jsonfile.close()

    #st.write('val: '+ str(val))
    
    #colors that field white if it is a space or if there is nothing in the value that can be split
    #into it parts which means there is nothing in the value and the value is not a space(this is why 
    # we use if not  val.split())

    # if not val.split() or val.isspace():
    #     st.write("val_split: "+ str(val.split()))
    if not val.split() or val.isspace():
        #st.write("val_split: "+ str(val.split()))
        #st.write('val: '+ str(val))
        #st.write('empty:'+ str(val))
        return colour.Color(data['EMPTY']).rgb

    if not color:
        #print('nonempty:'+ str(val))
        return colour.Color(data['NON-EMPTY']).rgb

    comma_split = val.split(",")
    # can be a number like 1,123 or something
    #TODO: Figure out what this is supposed to be? Three separate numbers?
    #maybe a date? Buut why are the commas removed + replaced with nothing?
    #Shouldnt there be date-specific separators
    if any([len(x) == 3 for x in comma_split]) and not any([x.isalpha() for x in val]):
        val = re.sub(",", "", val)

    #if val is a non-integer number with numbers before + after comma
    elif len(comma_split) == 2 and not any([x.isalpha() for x in val]):
        val = re.sub(",", ".", val)

    """
    else:
        for x in comma_split:
            parse_cell(x, color=True)
    """

    val = val.lstrip().rstrip()
    #print('val: '+str(val))

    try:
        int(val)
        #print('int:'+ str(val))
        return colour.Color(data['INTEGER']).rgb
    except ValueError:
        pass
    try:
        float(val)
        #print('float:'+ str(val))
        return colour.Color(data['FLOAT']).rgb
    except ValueError:
        pass
    if str(data['differentiate_times'])=="True":
        try:
            datetime.time.fromisoformat(val)
            #print('time :'+ str(val))
            return colour.Color(data['TIME']).rgb
        except ValueError:
            pass
    if str(data['differentiate_dates'])=="True":
        try:
            dateutil.parser.parse(val, parserinfo=customDateParserInfo())
            #print('date :'+ str(val))
            return colour.Color(data['DATE']).rgb

        except ValueError:
            pass
        except TypeError:
            pass
        except OverflowError:
            pass
    #This prevents the error message 'OverflowError: Python int too large to convert to C long'


    if val.isupper() & (str(data['differentiate_all_uppercase'])=="True"):
        #print('isupper :'+ str(val))
        return colour.Color(data['STRING_UPPER']).rgb
    elif val.islower() & (str(data['differentiate_all_lowercase'])=="True"):
        #print('islower :'+ str(val))
        return colour.Color(data['STRING_LOWER']).rgb
    elif val.istitle() & (str(data['differentiate_all_titles'])=="True"):
        #print('title :'+ str(val))
        return colour.Color(data['STRING_TITLE']).rgb


    #print('generic :'+ str(val))
    #return string_color
    #st.write(data['STRING_GENERIC'])
    # if data['separator_bars']=='True':
    #     return colour.Color(data['STRING_GENERIC']).rgb, colour.Color(data['EMPTY']).rgb
    return colour.Color(data['STRING_GENERIC']).rgb
