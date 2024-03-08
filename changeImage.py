#!/usr/bin/env python3

# This script will process images using the PIL library
# Changing image resolution to from 3000x2000 to 600x400 pixel.
# Changing format from .TIFF to .JPEG

import os
from PIL import Image

# Get username from environment variable
# user = os.getenv('USER')
user = os.environ.get('USER')

# assign image directory to a variable
# img_dir = '/img/'.format(user)
img_dir = '/home/{}/supplier-data/images/'.format(user)

# Parse through all images
for dir_images in os.listdir(img_dir):
    # Check if the file is a TIFF image
    if dir_images.lower().endswith('.tiff') and not dir_images.startswith('.'):
        # Create an absolute path for images
        # img_path = img_dir + dir_images
        img_path = os.path.join(img_dir, dir_images)
        # Get the name of each image starting from the first image
        path = os.path.splitext(img_path)[0]
        # Open images
        with Image.open(img_path) as openedimages:
            # New variable with same path as original images but with .jpeg extension
            new_jpeg_path = '{}.jpeg'.format(path)
            # Convert images to RGB, resize and save image with JPEG format
            openedimages.convert('RGB').resize((600, 400)).save(new_jpeg_path, "JPEG")
        print('Processed:', dir_images)