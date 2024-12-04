# Python Image Filter App
## By Timothy Sims

## App Introduction
This project was created using Python Streamlit library.
It takes an image uploaded by the user and applies the selected filter to it.
The images must be jpg, jpeg, or png.

## App Filters
The filters included are greyscale, black and white, blur, negative, darken, edge detection, and rotation.
Filters blur, rotation, edge detection, black and white, and darken all take input in the form of a slider to adjust their respective input values.
The negative and greyscale filters take no input from the user.

## Running and using the app
In order to run the app, open a terminal and navigate to the folder that contains PythonImageEditor.py
Then type streamlit run .\PythonImageEditor.py
Streamlit will open a tab within your browswer. Next upload an image to apply filters to. Sample images are saved under the Images folder.
When you are done and want to save the image, click the download button. The filtered image will be saved to the Output folder.