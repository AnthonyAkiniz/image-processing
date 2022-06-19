#########################################################################################
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * #
# * ################################################################################# * #
# * #                          Image Resizer                                        # * #
# * #                          project by: Anthony Akiniz                           # * #
# * #                          github.com/anthonyakiniz                             # * #
# * ################################################################################# * #
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * #
#########################################################################################
# Info:                                                                                 #
# Batch resize images.                                                                  #
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
# Launch by clicking run button in top right in VSCode or: py -3 resizer.py             #
#########################################################################################

from PIL import Image, ImageFilter

# batch resizing one image at varying sizes max specified while maintaining aspect ratio to avoid distortion
img = Image.open("./Nature/nature1.jpg")
img.thumbnail((150, 150))
img.save('./Nature-Resized/nature1_150x150.jpg')

img = Image.open("./Nature/nature1.jpg")
img.thumbnail((400, 400))
img.save('./Nature-Resized/nature1_400x400.jpg')

img = Image.open("./Nature/nature1.jpg")
img.thumbnail((800, 800))
img.save('./Nature-Resized/nature1_800x800.jpg')

img = Image.open("./Nature/nature1.jpg")
img.thumbnail((1920, 1080))
img.save('./Nature-Resized/nature1_1920x1080.jpg')

# batch resizing all at same size to max 400x400 while maintaining aspect ratio to avoid distortion
# an 800x800 image to 400x400 will be 400x400, however 2652x3976 will be 267x400 to maintain aspect ratio
img = Image.open("./People/people1.jpg")
img.thumbnail((400, 400))
img.save('./People-Resized/people1_400x400.jpg')

img = Image.open("./People/people2.jpg")
img.thumbnail((400, 400))
img.save('./People-Resized/people2_400x400.jpg')

img = Image.open("./People/people3.jpg")
img.thumbnail((400, 400))
img.save('./People-Resized/people3_400x400.jpg')

img = Image.open("./People/people4.jpg")
img.thumbnail((400, 400))
img.save('./People-Resized/people4_400x400.jpg')

# optional displays pop up preview of last converted image
img.show()
