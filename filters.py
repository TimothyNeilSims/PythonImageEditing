# Timothy Sims COP2034 Final Project


# imports necessary libraries, streamlit not needed since this is just the functions
# originally had matplotlib.pyplot as well but I was able to complete this using only these libraries
import cv2
import numpy as np
from PIL import Image


# originally I had made these all in separate .py files and had used streamlits pages to have each function on its own separate page
# when I was reviewing the instructions to see if I missed anything I changed it to this format with a selection on the side and all functions together in a single .py file as instructed
def blur(image,intensity):
    # converts img into an array so that cv2 can modify it
    img = np.array(image)
    # ksize in docs takes separate values but I made them the same (intensity) since there is no noticeable difference in the filter
    ksize = (intensity,intensity)
    # applies the cv2.blur to the image with the input from the slider
    imageblur = cv2.blur(img,ksize)
    # return statement to give back the 
    return imageblur

def grey(image):
    img = np.array(image)
    # RGB2GRAY used since opened with PIL it is RGB not BGR as in class, no conversion needed
    imggrey = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    return imggrey

def negative(image):
    # again converts to array
    img = np.array(image)
    # for loop to subtract each value of the image from 255, range 3 used so it will cycle through 0 red, 1 green, 2 blue and stop before 3
    for i in range(3):
        img[:,:,i] = 255 - img[:,:,i]
    return img

def darken(image,intensity):
    img = np.array(image)
    # sets the value of pixels below the intensity cuttoff to 0 making the image darker
    img[img<intensity]=0
    return img

# takes angle of rotation as input, min 0(no change) max 360(complete rotation so no change)
def rotate(image,rotation,crop):
    # uses PIL Image.rotate to rotate the image since cv2 would not allow for a slider input
    # Originally I used the code from class, but it cropped the edges of the picture outside of the origianl files boundaries
    # So I looked up the documentation to allow the image to retain its original shape but with rotation
    if crop == 'Yes':
        imagerotate = image.rotate(rotation)
    else:
        imagerotate = image.rotate(rotation, Image.NEAREST,expand = 1)
    # changes from PIL image to array so that it stays consistent with the other functions
    # done after the rotation so Image.rotate can still be applied
    img = np.array(imagerotate)
    return img

# takes lower and upper thresholds as arguments, tried only using one for both like in blur, but decided to keep the two input sliders
def edge_detection(image,threshold1,threshold2):
    img = np.array(image)
    # pretty much the same we used in class but will user input to change both lower and upper
    imgedge = cv2.Canny(img,threshold1,threshold2)
    return imgedge

def black_and_white(image,intensity):
    img = np.array(image)
    # first converted to greyscale
    imggrey = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    # applies threshold to the greyscale image, values below the threshold will be set to 0 (black) and those above will be set to 255 (white)
    # index [1] used since .threshold gives a tuple
    imgbw = cv2.threshold(imggrey, intensity, 255, cv2.THRESH_BINARY)[1]
    return imgbw