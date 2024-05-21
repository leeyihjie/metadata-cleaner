import streamlit as st
from PIL import Image
import piexif
import base64
import os

from helper_functions.io_helper import get_project_path


# Initialise project folder path
path = get_project_path()

# Initialise path for images to be cleaned and de-metafied
path= os.path.join(path, 'images_to_clean')

print(path)

# def uploadImage():
    # open method used to open different extension image file 
    # im = Image.open(r"C:\Users\System-Pc\Desktop\ybear.jpg")  


# To run the application
# if __name__ == "__main__":
#
