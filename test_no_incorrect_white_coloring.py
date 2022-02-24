import sys
sys.path.append('C:\\Users\\Ella\\Ella-Kopie\\Studium\\Semester9\\Job\\Mondrian extension for CSV Visualization\\mondrian')
from mondrian.visualization import manipulate_created_image, create_image, table_as_image_better,manipulate_created_image

#tests whether an image that should not be colored white is completely white
def test_no_incorrect_white_coloring():
    result_img= table_as_image_better('C:\\Users\\Ella\\Ella-Kopie\\Studium\\Semester9\\Job\\Mondrian extension for CSV Visualization\\comma_quotationMark_quotatioMark_test.csv', delimiter =',', quotechar='"', escapechar = '"')
    white = [255,255,255]
    all_white =True
    for line in result_img:
        for color in line:
            if color != white:
                all_white = False
                break
        break

    assert all_white == False
            
#tests whether an image that should not be colored white is partly white white

    white = [255,255,255]
    partly_white =False
    for line in result_img:
        for color in line:
            if color == white:
                partly_white = True
                break
        break

    assert partly_white == False
            
    


