# csv-coloring - Visualizing csv files
Visualize csv file dialects

Sometimes csv files are displayed with such garbled meaning, that they appear to have been by aliens. But the reason may be just a simple dialect mishap, that caused the problem. Problem is, there are many, many possible dialects. And while very good programs like clevercsv(https://clevercsv.readthedocs.io/en/latest/) have taken a crack at it, they estimate the dialect depending on content. This solution allows for testing any dialects you suspect the csv file might have and directly displaying the result by generating images whose pixels have ben colored according to data types. This way, nonsensical solutions are identified immediately.

- add example of good generated result + bad generated result

# Using the app
This app requires the installation of the steamlit package of at least version 1.3.0(https://github.com/streamlit/streamlit).

Simply install the app, move to the installation folder and type  "streamlit run .\streamlit_start.py" in your command-line.

# Features

- try all kind of dialects, one after another or several at once
- resize your images
- color different data types in different colors
- choose what algorithm to resample you
- faster display via web app

# Issues

- the program cannot yet identify title strings

# Extension ideas
I have added some more specific extension ideas as TODOs in the code itself. Possible improvements in general are

- improving the algorithm for putting as many pictures next to each other as the available space allows for wothout shrinking the images
- allowing for addition of additional dialect symbols to choose from

