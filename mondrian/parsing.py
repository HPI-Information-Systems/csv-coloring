import datetime
#from backports.datetime_fromisoformat import MonkeyPatch
#MonkeyPatch.patch_fromisoformat()

import json
import streamlit as st
import matplotlib.colors as colors
#from . import colors as colors
#import colour as colors
import colour
import dateutil.parser
import re
import sys
sys.path.append('C:\\Users\\Ella\\Ella-Kopie\\Studium\\Semester9\\Job\\Mondrian extension for CSV Visualization\\mondrian')

class CellType_test():
#     # EMPTY = colors.RGB_WHITE
#     # NON_EMPTY = colors.RGB_BLACK
#     # INTEGER = colors.RGB_LIGHTPINK
#     # FLOAT = colors.RGB_DARKPINK
#     # TIME = colors.RGB_MEDIUMORCHID
#     # DATE = colors.RGB_MEDIUMPURPLE
#     # STRING_UPPER = colors.RGB_LIME
#     # STRING_LOWER = colors.RGB_LIMEGREEN
#     # STRING_TITLE = colors.RGB_SPRINGGREEN
#     # STRING_GENERIC = colors.RGB_LIGHTGREEN
    
#     # #TODO: figure out if the lack of the RGB signifier with the colrs poses a problem
#     # EMPTY = colour.Color("white").rgb
#     # NON_EMPTY = colour.Color("black").rgb
#     # INTEGER = colour.Color("lightpink").rgb
#     # #am using mediumvioletred as replacement for darkpink, hope that comes closest in spirit
#     # FLOAT = colour.Color("mediumvioletred").rgb
#     # TIME = colour.Color("mediumorchid").rgb
#     # DATE = colour.Color("mediumpurple").rgb
#     # STRING_UPPER = colour.Color("lime").rgb
#     # STRING_LOWER = colour.Color("limegreen").rgb
#     # STRING_TITLE = colour.Color("springgreen").rgb
#     # STRING_GENERIC = colour.Color("lightgreen").rgb

    def _init_(self):
        self.EMPTY = colour.Color("white").rgb
        self.NON_EMPTY = colour.Color("black").rgb
        self.INTEGER = colour.Color("lightpink").rgb
         #am using mediumvioletred as replacement for darkpink, hope that comes closest in spirit
        self.FLOAT = colour.Color("mediumvioletred").rgb
        self.TIME = colour.Color("mediumorchid").rgb
        self.DATE = colour.Color("mediumpurple").rgb
        self.STRING_UPPER = colour.Color("lime").rgb
        self.STRING_LOWER = colour.Color("limegreen").rgb
        self.STRING_TITLE = colour.Color("springgreen").rgb
        self.STRING_GENERIC = colour.Color("lightgreen").rgb

    #     # self.EMPTY = colors.RGB_WHITE
    #     # self.NON_EMPTY = colors.RGB_BLACK
    #     # self.INTEGER = colors.RGB_LIGHTPINK
    #     # self.FLOAT = colors.RGB_DARKPINK
    #     # self.TIME = colors.RGB_MEDIUMORCHID
    #     # self.DATE = colors.RGB_MEDIUMPURPLE
    #     # self.STRING_UPPER = colors.RGB_LIME
    #     # self.STRING_LOWER = colors.RGB_LIMEGREEN
    #     # self.STRING_TITLE = colors.RGB_SPRINGGREEN
    #     # self.TIMESTRING_GENERIC = colors.RGB_LIGHTGREEN
    
    def EMPTY(self,value):
        self._EMPTY = value

    def NON_EMPTY(self,value):
        self._NON_EMPTY = value

    def INTEGER(self,value):
        self._INTEGER = value

    def FLOAT(self,value):
        self._FLOAT = value
    
    def TIME(self,value):
        self._TIME = value

    def DATE(self,value):
        self._DATE = value

    def STRING_TITLE(self,value):
        self._STRING_TITLE = value
    
    def STRING_UPPER(self,value):
        self._STRING_LOWER = value

    def STRING_LOWER(self,value):
        self._STRING_LOWER = value

    def STRING_GENERIC(self,value):
        self._STRING_GENERIC = value

    def EMPTY(self):
        return self._EMPTY

    def NON_EMPTY(self):
        return self._NON_EMPTY

    def INTEGER(self):
        return self._INTEGER

    def FLOAT(self):
        return self._FLOAT
    
    def TIME(self):
        return self._TIME

    def DATE(self):
        return self._DATE

    def STRING_TITLE(self):
        return self._STRING_TITLE
    
    def STRING_UPPER(self):
        return self._STRING_LOWER

    def STRING_LOWER(self):
        return self._STRING_LOWER

    def STRING_GENERIC(self):
        return self._STRING_GENERIC


#class for setting custom cell types
#

class CellType():
    # #TODO: figure out if the lack of the RGB signifier with the colrs poses a problem
    EMPTY = colour.Color("white").rgb
    NON_EMPTY = colour.Color("black").rgb
    INTEGER = colour.Color("lightpink").rgb
    #am using mediumvioletred as replacement for darkpink, hope that comes closest in spirit
    FLOAT = colour.Color("mediumvioletred").rgb
    TIME = colour.Color("mediumorchid").rgb
    DATE = colour.Color("mediumpurple").rgb
    STRING_UPPER = colour.Color("lime").rgb
    STRING_LOWER = colour.Color("limegreen").rgb
    STRING_TITLE = colour.Color("springgreen").rgb
    STRING_GENERIC = colour.Color("lightgreen").rgb

     #EMPTY = colour.Color("white").rgb
    # NON_EMPTY = colour.Color("black").rgb
    # INTEGER = colour.Color("lightpink").rgb
    # #am using mediumvioletred as replacement for darkpink, hope that comes closest in spirit
    # FLOAT = colour.Color("mediumvioletred").rgb
    # TIME = colour.Color("mediumorchid").rgb
    # DATE = colour.Color("mediumpurple").rgb
    # STRING_UPPER = colour.Color("lime").rgb
    # STRING_LOWER = colour.Color("limegreen").rgb
    # STRING_TITLE = colour.Color("springgreen").rgb
    # STRING_GENERIC = colour.Color("lightgreen").rgb

    #EMPTY = colors.RGB_WHITE
    #NON_EMPTY = colors.RGB_BLACK
    #INTEGER = colors.RGB_LIGHTPINK
    #FLOAT = colors.RGB_DARKPINK
    #TIME = colors.RGB_MEDIUMORCHID
    #DATE = colors.RGB_MEDIUMPURPLE
    #STRING_UPPER = colors.RGB_LIME
    #STRING_LOWER = colors.RGB_LIMEGREEN
    #STRING_TITLE = colors.RGB_SPRINGGREEN
    #STRING_GENERIC = colors.RGB_LIGHTGREEN
    
    
    # def _init_(self):
    #     self.EMPTY = colour.Color("white").rgb
    #     self.NON_EMPTY = colour.Color("black").rgb
    #     self.INTEGER = colour.Color("lightpink").rgb
    #     #am using mediumvioletred as replacement for darkpink, hope that comes closest in spirit
    #     self.FLOAT = colour.Color("mediumvioletred").rgb
    #     self.TIME = colour.Color("mediumorchid").rgb
    #     self.DATE = colour.Color("mediumpurple").rgb
    #     self.STRING_UPPER = colour.Color("lime").rgb
    #     self.STRING_LOWER = colour.Color("limegreen").rgb
    #     self.STRING_TITLE = colour.Color("springgreen").rgb
    #     self.STRING_GENERIC = colour.Color("lightgreen").rgb

    #     # self.EMPTY = colors.RGB_WHITE
    #     # self.NON_EMPTY = colors.RGB_BLACK
    #     # self.INTEGER = colors.RGB_LIGHTPINK
    #     # self.FLOAT = colors.RGB_DARKPINK
    #     # self.TIME = colors.RGB_MEDIUMORCHID
    #     # self.DATE = colors.RGB_MEDIUMPURPLE
    #     # self.STRING_UPPER = colors.RGB_LIME
    #     # self.STRING_LOWER = colors.RGB_LIMEGREEN
    #     # self.STRING_TITLE = colors.RGB_SPRINGGREEN
    #     # self.TIMESTRING_GENERIC = colors.RGB_LIGHTGREEN
    
    # def EMPTY(self,value):
    #     self._EMPTY = value

    # def NON_EMPTY(self,value):
    #     self._NON_EMPTY = value

    # def INTEGER(self,value):
    #     self._INTEGER = value

    # def FLOAT(self,value):
    #     self._FLOAT = value
    
    # def TIME(self,value):
    #     self._TIME = value

    # def DATE(self,value):
    #     self._DATE = value

    # def STRING_TITLE(self,value):
    #     self._STRING_TITLE = value
    
    # def STRING_UPPER(self,value):
    #     self._STRING_LOWER = value

    # def STRING_LOWER(self,value):
    #     self._STRING_LOWER = value

    # def STRING_GENERIC(self,value):
    #     self._STRING_GENERIC = value

    # def EMPTY(self):
    #     return self._EMPTY

    # def NON_EMPTY(self):
    #     return self._NON_EMPTY

    # def INTEGER(self):
    #     return self._INTEGER

    # def FLOAT(self):
    #     return self._FLOAT
    
    # def TIME(self):
    #     return self._TIME

    # def DATE(self):
    #     return self._DATE

    # def STRING_TITLE(self):
    #     return self._STRING_TITLE
    
    # def STRING_UPPER(self):
    #     return self._STRING_LOWER

    # def STRING_LOWER(self):
    #     return self._STRING_LOWER

    # def STRING_GENERIC(self):
    #     return self._STRING_GENERIC

class customDateParserInfo(dateutil.parser.parserinfo):
    JUMP = [' ', '.', ',', ';', '-', '/', "'"]


#differentiate_all_uppercase, differentiate_all_lowercase and differentiate_all_titles, if true, mean that you 
# want
#1. differentiate_all_uppercase: words that only contain uppercase letters + plus non-letter signs
#2. differentiate_all_lowercase: words that only contain lowercase letters + plus non-letter signs
#3. differentiate_all_titles: strings where every word starts with an uppercase letter
# to be differently coloured by the algorithm

# def parse_cell(val, color=False, differentiate_all_uppercase=False, differentiate_all_lowercase=False, 
# differentiate_all_titles=False,string_color=colour.Color("lightgreen").rgb, int_color=colour.Color("lightpink").rgb,float_color=colour.Color("mediumvioletred").rgb):
def parse_cell(val, color=False):    
    #st.write(val)
    with open("C:\\Users\\Ella\\Ella-Kopie\\Studium\\Semester9\\Job\\Mondrian extension for CSV Visualization\\mondrian\\colors.json", "r") as jsonfile:
        data = json.load(jsonfile) # Reading the file
        #print("Read successful")
        jsonfile.close()

    #print('color: '+ str(color))
    #print('val: '+ str(val))
    
    #colors that field white if it is a space or if there is nothing in the value that can be split
    #into it parts which means there is nothing in the value and the value is not a space(this is why 
    # we use if not  val.split())

#llolololollo
#lolokokoklo



    # if not val.split():
    #     st.write("val_split: "+ str(val.split()))
    if not val.split() or val.isspace():
        #print('empty:'+ str(val))
        #return CellType.EMPTY
        return colour.Color(data['EMPTY']).rgb

    if not color:
        #print('nonempty:'+ str(val))
        #return CellType.NON_EMPTY
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
        #return CellType.INTEGER
        #return int_color
        return colour.Color(data['INTEGER']).rgb
    except ValueError:
        pass
    try:
        float(val)
        #print('float:'+ str(val))
        #return CellType.FLOAT
        #return float_color
        return colour.Color(data['FLOAT']).rgb
    except ValueError:
        pass
    try:
        datetime.time.fromisoformat(val)
        #print('time :'+ str(val))
        #return CellType.TIME
        return colour.Color(data['TIME']).rgb
    except ValueError:
        pass
    try:
        dateutil.parser.parse(val, parserinfo=customDateParserInfo())
        #print('date :'+ str(val))
        #return CellType.DATE
        return colour.Color(data['DATE']).rgb

    except ValueError:
        pass
    except TypeError:
        pass
    #This prevents the error message 'OverflowError: Python int too large to convert to C long'
    except OverflowError:
        pass

    if val.isupper() & (str(data['differentiate_all_uppercase'])=="True"):
        print('isupper :'+ str(val))
        #return CellType.STRING_UPPER
        return colour.Color(data['STRING_UPPER']).rgb
    elif val.islower() & (str(data['differentiate_all_lowercase'])=="True"):
        print('islower :'+ str(val))
        #return CellType.STRING_LOWER
        return colour.Color(data['STRING_LOWER']).rgb
    elif val.istitle() & (str(data['differentiate_all_titles'])=="True"):
        print('title :'+ str(val))
        #return CellType.STRING_TITLE
        return colour.Color(data['STRING_TITLE']).rgb

    #print('generic :'+ str(val))
    #return CellType.STRING_GENERIC
    #return string_color
    #st.write(data['STRING_GENERIC'])
    return colour.Color(data['STRING_GENERIC']).rgb

# def parse_cell(val, color=False, differentiate_all_uppercase=False, differentiate_all_lowercase=False, 
# differentiate_all_titles=False,string_color=colour.Color("lightgreen").rgb, int_color=colour.Color("lightpink").rgb,float_color=colour.Color("mediumvioletred").rgb):
#     #print('color: '+ str(color))
#     #print('val: '+ str(val))
#     if not val.split() or val.isspace():
#         #print('empty:'+ str(val))
#         return CellType.EMPTY

#     if not color:
#         #print('nonempty:'+ str(val))
#         return CellType.NON_EMPTY

#     comma_split = val.split(",")
#     # can be a number like 1,123 or something
#     #TODO: Figure out what this is supposed to be? Three separate numbers?
#     #maybe a date? Buut why are the commas removed + replaced with nothing?
#     #Shouldnt there be date-specific separators
#     if any([len(x) == 3 for x in comma_split]) and not any([x.isalpha() for x in val]):
#         val = re.sub(",", "", val)

#     #if val is a non-integer number with numbers before + after comma
#     elif len(comma_split) == 2 and not any([x.isalpha() for x in val]):
#         val = re.sub(",", ".", val)

#     """
#     else:
#         for x in comma_split:
#             parse_cell(x, color=True)
#     """

#     val = val.lstrip().rstrip()
#     #print('val: '+str(val))

#     try:
#         int(val)
#         #print('int:'+ str(val))
#         #return CellType.INTEGER
#         return int_color
#     except ValueError:
#         pass
#     try:
#         float(val)
#         #print('float:'+ str(val))
#         #return CellType.FLOAT
#         return float_color
#     except ValueError:
#         pass
#     try:
#         datetime.time.fromisoformat(val)
#         #print('time :'+ str(val))
#         return CellType.TIME
#     except ValueError:
#         pass
#     try:
#         dateutil.parser.parse(val, parserinfo=customDateParserInfo())
#         #print('date :'+ str(val))
#         return CellType.DATE
#     except ValueError:
#         pass
#     except TypeError:
#         pass
#     #This prevents the error message 'OverflowError: Python int too large to convert to C long'
#     except OverflowError:
#         pass

#     if val.isupper() & differentiate_all_uppercase:
#         print('isupper :'+ str(val))
#         return CellType.STRING_UPPER
#     elif val.islower() & differentiate_all_lowercase:
#         print('islower :'+ str(val))
#         return CellType.STRING_LOWER
#     elif val.istitle() & differentiate_all_titles:
#         print('title :'+ str(val))
#         return CellType.STRING_TITLE

#     #print('generic :'+ str(val))
#     #return CellType.STRING_GENERIC
#     return string_color