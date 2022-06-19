#########################################################################################
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * #
# * ################################################################################# * #
# * #                          JPG to PNG Batch Converter                           # * #
# * #                          project by: Anthony Akiniz                           # * #
# * #                          github.com/anthonyakiniz                             # * #
# * ################################################################################# * #
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * #
#########################################################################################
# Info:                                                                                 #
# Batch converts jpg to png files.                                                      #
#                                                                                       #
# Requirements:                                                                         #
# python3 -m pip install --upgrade pip                                                  #
# python3 -m pip install --upgrade Pillow                                               #
# verify if you already have it globally: pip list                                      #
# documentation: https://pillow.readthedocs.io/en/stable/index.html                     #
#                                                                                       #
# Guide:                                                                                #
# Rename project folder to: image-processing                                            #
# Change path to project folder: cd image-processing                                    #
# in terminal run: py -3 jpg_to_png.py Nature/ Nature-PNG/                              #
# in terminal run: py -3 jpg_to_png.py People/ People-PNG/                              #
#########################################################################################

import sys
import os
from PIL import Image

# grab first and second argument
path = sys.argv[1]
directory = sys.argv[2]

# check if output directory folder exists, if not makedirs = make the directory
if not os.path.exists(directory):
    os.makedirs(directory)


for filename in os.listdir(path):
    clean_name = os.path.splitext(filename)[0]  # splits name from extension
    img = Image.open(f'{path}{filename}')
    # added the / in case user doesn't enter it. You may want to check for this and add or remover it.
    img.save(f'{directory}/{clean_name}.png', 'png')
    print('all done!')
