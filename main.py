import streamlit as st
from PIL import Image
import piexif
import base64
import os
import glob

from helper_functions.io_helper import get_project_path


# Initialise project folder path
projectPath = get_project_path()

# Initialise path for images to be cleaned and de-metafied
imagePath= os.path.join(projectPath, 'images_to_clean')


def loadImages():
    imageList = []
    for image in glob.glob(imagePath + "/*"):
        print(image)
        imageList.append(image)
    print(imageList)    
    return imageList

def cleanImages(listToClean):
     for image in listToClean:
        imageToClean = Image.open(image)

def run():
    iList = loadImages()
    cleanImages(iList)

# To run the application
if __name__ == "__main__":
    run()
