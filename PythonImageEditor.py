# Timothy Sims COP2034 Final Project

# imports streamlit and all functions from filters using * so the functions can be done without calling filters.blur ect
import streamlit as st
from filters import *



# create columns to separate the school logo and name, date, project title
# st.column uses a list so that the first column is 3 times the size of the second, this is to replicate format in the instructions
column1,column2=st.columns([3,1])
with column1:
    # used .title for larger size text
    st.title('Timothy Sims')
    st.title('Final Project COP2034')
    st.title('5/3/2023')
with column2:
    # displays the school logo saved in the folder
    st.image('Images/fau.png', caption='', use_column_width=True)
st.markdown('Thank you for a wonderful semester!')
# allows the user to upload a file as long as it is jpg jpeg or png, assigned a variable to call for use
userfile = st.file_uploader('Upload your image', type=['jpg', 'jpeg', 'png'])
# app name on the sidebar using title for larger font
st.sidebar.title('Final Project')
# description on sidebar using .write 
st.sidebar.write('Created using Python Streamlit library. Uses OpenCV, PIL, and NumPy. Supports jpg, jpeg, and png files')

# the following code will only run if a file has been uploaded
if userfile:
    # adds filter selection to the sidebar
    with st.sidebar:
        filters = st.radio('Convert your photo to:',('Original','Blur','Rotate','Darken','Edge Detection','Black and White','Negative','Greyscale'))
    #opens the image using PIL to be put into functions
    image = Image.open(userfile)
    # if statements which will decide which filter gets applied 
    if filters == 'Original':
        filtered = np.array(image)
        # Originally I had the download using cv2.imwrite use filtered directly, but I noticed at the end of my project that all the colors would be bgr instead of rgb when downloaded
        # I hadn't noticed sooner as I am colorblind and they still showed up normally on the app, only swapping color when saved using cv2.imwrite
        # I noticed this when implementing an original statement since I noticed there was one in the instructions
        # Luckily I'm not too colorblind that I couldn't even tell the differnce between the same color swapped image
        download = cv2.cvtColor(filtered,cv2.COLOR_RGB2BGR)
    elif filters == 'Blur':
        # adds a slider to change the intensity to the sidebar
        # .sidebar can be put before the element like slider, write, to put in sidebar
        intensity = st.sidebar.slider('Intensity: ', 1, 100)
        filtered = blur(image,intensity)
        download = cv2.cvtColor(filtered,cv2.COLOR_RGB2BGR)
    elif filters == 'Greyscale':
        # no sidebar added since it just converts to grey
        filtered= grey(image)
        # .cvtColor used here just for consistency since it will make no difference (that I can see at least)
        download = cv2.cvtColor(filtered,cv2.COLOR_RGB2BGR)
    elif filters == 'Rotate':
        # takes angle to rotate the image as arguement
        angle = st.sidebar.slider('Rotation angle: ', 0, 360)
        # choice added to retain the original ratio since I found how to adjust it to avoid cropping in the docs, originally in class our function would keep the orignal ratio and crop the excess areas off
        with st.sidebar:
            crop = st.radio('Would you like to retain the original image ratio?',('Yes','No'))
        filtered =rotate(image,angle,crop)
        download = cv2.cvtColor(filtered,cv2.COLOR_RGB2BGR)
    elif filters =='Negative':
        # no argument needed since it just takes negative of the image
        filtered = negative(image)
        download = cv2.cvtColor(filtered,cv2.COLOR_RGB2BGR)
    elif filters =='Darken':
        # slider for the darken intensity
        intensity = st.sidebar.slider('Intensity: ', 0, 255)
        filtered = darken(image,intensity)
        download = cv2.cvtColor(filtered,cv2.COLOR_RGB2BGR)
    elif filters =='Edge Detection':
        # creates 2 sliders since edge detection takes 2 arguments
        threshold1 = st.sidebar.slider('Lower Value: ', 0, 255)
        threshold2 = st.sidebar.slider('Upper Value: ', 0, 255)
        filtered = edge_detection(image,threshold1,threshold2)
        download = cv2.cvtColor(filtered,cv2.COLOR_RGB2BGR)
    elif filters =='Black and White':
        intensity = st.sidebar.slider('Intensity: ', 0, 255)
        filtered = black_and_white(image,intensity)
        # .cvtColor also used here for consistency even though I couldn't tell a difference
        download = cv2.cvtColor(filtered,cv2.COLOR_RGB2BGR)

    # creates new columns bewlow the upload button so they are properly aligned
    col1,col2=st.columns(2)
    with col1:
        # uses streamlit to display the images, can display both PIL(original image) and np.array(after the filters)
        st.image(image, caption='Original Image', use_column_width=True)
    with col2:
        st.image(filtered, caption='Filtered Image', use_column_width=True)
    # takes filename using .name from streamlit, st. not needed since userfile is a streamlit object
    name = userfile.name
    # name split at the file extension, indexed to only take what is before the extension to avoid having .png.png files
    # also accounts for filenames using '.' within them by taking all of the list except the final element which is the file extension
    filenamelist = name.split('.')[0:-1]
    # joins the elements of the set together into a string, this preserves any filenames with a '.' in them by joining them with it again while also avoiding having [] in the filename
    filename = '.'.join(filenamelist)
    # takes the final element of the string and indexes it at 0 since it is a list of a single element, string needed for naming the file
    filetype = name.split('.')[-1:][0]
    # placed in col2 directly below filted image
    with col2:
        if st.button('Download Filtered Image'):
            # {filters} is the filter selected on the sidebar, {filename} is the split userfile.name without the file extension, {filetype} is the type of file taken from [1] of the split
            # download is the filtered image after it has been swapped from rgb2bgr since that is what cv2.imwrite assumes it is
            filteredimage = cv2.imwrite(f'Output/{filters}_{filename}.{filetype}',download)
