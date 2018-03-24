import easygui
import os
from os import listdir
from os.path import isfile, join
from shutil import copyfile
import shutil
#Pick the folder where all the images are
path = easygui.diropenbox("Open Files", "Choose Image Directory")
#Make all the directories
#Images Directory
print("Making Directories")
directories = ["images", "output"]
count = 1
for directory in directories:
    print("Creating Directory " + str(count) + " of " + str(len(directories)))
    if not os.path.exists(path + "\\" + directory):
        os.makedirs(path + "\\" + directory)
    count = count + 1
#Copy all the images to /images
print("Copying Images")
#Get listing of all files
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
count = 1
for file in onlyfiles:
    print("Copying File " + str(count) + " of " + str(len(onlyfiles)))
    copyfile(path + "\\" + onlyfiles[count - 1], path + "\\images\\" + onlyfiles[count - 1])
    os.remove(path + "\\" + onlyfiles[count - 1])
    count = count + 1