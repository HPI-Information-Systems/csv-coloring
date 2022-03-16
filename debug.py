import sys
sys.path.append('C:\\Users\\Ella\\Ella-Kopie\\Studium\\Semester9\\Job\\Mondrian extension for CSV Visualization\\mondrian')
import pandas as pd
from mondrian.visualization import table_as_image_better, manipulate_created_image
import colour
import app 
import csv

image_all_same_color, image = manipulate_created_image(table_as_image_better("C:\\Users\\Ella\\Ella-Kopie\\Studium\\Semester9\\Job\\Mondrian extension for CSV Visualization\\all_data_types_test.csv", delimiter=',', quotechar='"', escapechar='"'), True)

#trollollooo
# fileObject = csv.reader('C:\\Users\\Ella\\Ella-Kopie\\Studium\\Semester9\\Job\\debug.tar\\csv\\SouthTrent_reduced_TravelTimes.csv')
# row_count = sum(1 for row in fileObject)
# special_characters = ['!', '"', '$', '#', '%', '&', '\'', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

# #file_path='C:\\Users\\Ella\\Ella-Kopie\\Studium\\Semester9\\Job\\debug.tar\\csv\\SouthTrent_reduced_TravelTimes.csv'
# #file =  app.load_data('C:\\Users\\Ella\\Ella-Kopie\\Studium\\Semester9\\Job\\debug.tar\\csv\\SouthTrent_reduced_TravelTimes.csv', row_count, ',')
# #file= app.load_data('C:\Users\Ella\Ella-Kopie\Studium\Semester9\Job\Mondrian extension for CSV Visualization\characters.csv')
# file_path='C:\\Users\\Ella\\Ella-Kopie\\Studium\\Semester9\\Job\\Mondrian extension for CSV Visualization\\characters.csv'
# #cols = pd.DataFrame([special_characters, '#'])
# #cols = pd.DataFrame()
# color=True
# table_as_image(file_path, ',', color).show()
# '''
# for i in range(0, len(special_characters)):                     # create image grid
#     #i am removing the part where we group the seapartors in columns depending on their position in the special_characters string
#         #we might need to add it again later in some way for display purposes

#         #assigning images ro dataframes is not going very swimmingly, so im going to abstain from it
#         #cols[f'{special_characters[i]}']=table_as_image(file_path, f'{special_characters[i]}', color=True)

#         #TODO: Solve current problem : -the data only gets registered + coolored as empty + nonempty, but none of the data types get colored in the 
#             #nonempty part
#         table_as_image(file_path, f'{special_characters[i]}', color)
# '''