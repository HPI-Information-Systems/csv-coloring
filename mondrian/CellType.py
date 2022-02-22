import colour

class CellType():
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

