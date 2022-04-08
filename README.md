# csv-coloring - Visualizing csv files

Sometimes csv files are displayed with such garbled meaning, that they appear to have been made by aliens. But it may be just a simple csv  dialect mishap that caused the problem. Problem is, there are many, many possible dialects. And while very good programs like clevercsv(https://clevercsv.readthedocs.io/en/latest/) have taken a crack at it, they estimate the dialect depending on content. This python app allows for testing any dialects you suspect the csv file might have and directly displaying the result by generating images whose pixels have been colored according to the data types inthe csv file. This way, nonsensical solutions are identified immediately.

# Installation

This app requires the installation of the streamlit package Version 1.3.0(https://github.com/streamlit/streamlit) and Python 3.9.7.

Simply install the app, move to the installation folder and type 

`streamlit run .\streamlit_start.py`

in your terminal.

# Using the app

When trying to figure out the dialect in your csv file, you can try looking at how the data types in the file are distributed in the file according to that dialect. For that, first choose "CSV Dialect Detection" and enter the path you want to investigate below. To pick the dialect to test, you can choose a delimiter, a quote character and an escape character. By default, only empty data(white color), string data, integer data and float data are differentiated with colors. We are trying this on the file test_display_more_lines_than_img_height_200.csv. Just tick the labeled boxes choose "," as delimiter and """ as quote and escape characters and press the "Create Visualization" button.

![](https://github.com/HPI-Information-Systems/csv-coloring/blob/main/images/wrong_coloring.PNG)

This color distribution looks very odd. But if we choose "," as delimiter, "'" as quote character and "$" as escape character and press "Create Visualization" again, then the data types are distributed more evenly which makes the dialect much morelikely to be correct.

![](https://github.com/HPI-Information-Systems/csv-coloring/blob/main/images/correct_weird_coloring.PNG)

If more information is needed, you can also tick a box to also mark dates, times, uppercase strings, lowercase strings, and/or  titles with their own color, as seen below on the same file for the same characters as the last picture

![](https://github.com/HPI-Information-Systems/csv-coloring/blob/main/images/good_coloration_more_colors.PNG)

The specific color can be changed separately for each data type in the sidebar

![](https://github.com/HPI-Information-Systems/csv-coloring/blob/main/images/Unbenannt.PNG)

# Features
There are also all kinds of other  features

- try several character combinations at once
- resize your images
- color different data types in different colors
- change these colors as you want
- choose what algorithm to resample the image created from your csv table
- fast display via caching
- choose to only show certain rows of a csv file
- divide the image with horizontal black bars to show where rows end

# Issues
If you have an interest in working on the program, you can help with the following issues

- The program cannot yet identify title string data as title strings(as determined by Python's istitle() function)


# Extension ideas
I have added some more specific extension ideas as TODOs in the code itself. Possible improvements in general are

- writing tests
- improving the algorithm for putting as many pictures next to each other as the available space allows for without shrinking the images
- allowing for addition of additional dialect symbols to choose from 
- show all rows with different distributions of data types in the image generated from the file, and show each approximately as often in the number of displayed pixels as they appear in the original file

