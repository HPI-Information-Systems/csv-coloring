# csv-coloring - Visualizing csv files
Visualize csv file dialects

Sometimes csv files are displayed with such garbled meaning, that they appear to have been by aliens. But the reason may be just a simple dialect mishap, that caused the problem. Problem is, there are many, many possible dialects. And while very good programs like clevercsv(https://clevercsv.readthedocs.io/en/latest/) have taken a crack at it, they estimate the dialect depending on content. This pythin app allows for testing any dialects you suspect the csv file might have and directly displaying the result by generating images whose pixels have ben colored according to data types. This way, nonsensical solutions are identified immediately.

# Installation
This app requires the installation of the streamlit package Version 1.3.0(https://github.com/streamlit/streamlit) and Python 3.9.7.

Simply install the app, move to the installation folder and type 

`streamlit run .\streamlit_start.py`

in your terminal.

# Using the app
When trying to figure out the dialect in your csv file, you can try how the data types in the file are distributed in the file according to that dialect. For that first choose "CSV Dialect Detection" and enter the path you want to investigate below. To pick the dialect to test, you can choose a delimiter, a quote character and an escape character. By default, only empty data, string data, integer data and float data are differentiated with colors. We are trying this on the file April_2015_published.csv. Just press the "Create Visualization" button.

![](https://github.com/HPI-Information-Systems/csv-coloring/blob/main/images/wrong_coloring.PNG)

This color distribution looks very odd. But if we use ... and press "Create Visualization" again, then the lines  have the same data types which makes the dialect much morelikely to be correct.

If more information is needed, you can also tick a box to also mark dates, times, uppercase strings, lowercase strings, and  titles with their own color, as seen below on the same file.

-white spaces in image mean unidentified data type or irregular row length

# Features
There are also all kinds of other  features

- try several dialects at once
- resize your images
- color different data types in different colors
- change these colors as you want!
- choose what algorithm to resample you
- faster display via web app
- only show certain rows of csv file
- divide the image with horizontal or vertical black bars to show where rows and/or columns end

# Issues
If you have an interest in working on the program, you can help with the folloing issues

- The program cannot yet identify title string data as title strings(as determined by Python's istitle() function)


# Extension ideas
I have added some more specific extension ideas as TODOs in the code itself. Possible improvements in general are

- write tests
- improving the algorithm for putting as many pictures next to each other as the available space allows for wothout shrinking the images
- allowing for addition of additional dialect symbols to choose from 
- show all rows with different distributions of data types in the image generated from the file, and show each approximately as often in the number of displayed pixels as they appear in the original file

