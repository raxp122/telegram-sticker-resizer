from PIL import Image
import os
from os import listdir
from os.path import isfile, join
from pathlib import Path

# generate directories
try:
    os.mkdir("Input")
except OSError:
    print("Failed Input directory creation or directory already exists")
else:
    print("Directory Input created")
try:
    os.mkdir("Output")
except OSError:
    print("Failed Output directory creation or directory already exists")
else:
    print("Directory Output created")

# get names of files in Input folder
onlyfiles = [f for f in listdir("Input") if isfile(join("Input", f))]

# set the size of the image for telegram stickers
max_side = 512

# resize every file in Input folder and save in Output folder
for file in onlyfiles:
    # open file
    img = Image.open('Input/' + file)
    if img.size[0] >= img.size[1]:
        width = max_side
        height = int((max_side / img.size[0]) * img.size[1])
        size = width, height
    elif img.size[1] > img.size[0]:
        width = int((max_side / img.size[1]) * img.size[0])
        height = max_side
        size = width, height
    # get name without extension
    name = Path(file).stem
    # resize the image use NEAREST if the image is pixelated (Ex: pixel art) or ANTIALIAS for smoother images
    img = img.resize(size, Image.NEAREST)
    # save resized image in .png to mantain transparency
    img.save("Output/" + name + ".png", "PNG")
