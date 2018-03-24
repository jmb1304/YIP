import easygui
import os
from os import listdir
from shutil import copyfile
from color import colors
import shutil

#Pick the folder where all the images are
path = easygui.diropenbox("Choose Image Directory")
vname = easygui.enterbox("Enter Volume Name")
#Make all the directories

#Images Directory
print(colors.OKGREEN + "Making Work Directories" + colors.ENDC)
directories = ["images", "output", "error"]
count = 1
for directory in directories:
    print("Creating Directory " + str(count) + " of " + str(len(directories)))
    if not os.path.exists(path + "\\" + directory):
        os.makedirs(path + "\\" + directory)
    count = count + 1

#Copy all the images to /images
print(colors.OKGREEN + "Copying Images" + colors.ENDC)
#Get listing of all files
onlyfiles = [f for f in listdir(path) if os.path.isfile(os.path.join(path, f))]
count = 1
for file in onlyfiles:
    print("Copying File " + str(count) + " of " + str(len(onlyfiles)))
    filename = file.split(".")
    suffix = filename[len(filename) - 1]
    if suffix.lower() == "jpg":
        copyfile(path + "\\" + file, path + "\\images\\img" + str(count) + ".jpg")
        os.remove(path + "\\" + file)
    else:
        print(colors.FAIL + file + " skipped due to unsupported format." + colors.ENDC)
        copyfile(path + "\\" + file, path + "\\error\\" + file)
        os.remove(path + "\\" + file)
    count = count + 1

#Generate Output Directories
print(colors.OKGREEN + "Making Output Directories" + colors.ENDC)
directories = ["Image"]
count = 1
print("Creating Directory " + str(count) + " of " + str(len(directories)))
if not os.path.exists(path + "\\output\\" + vname):
    os.makedirs(path + "\\output\\" + vname)
    count = count + 1
for directory in directories:
    print("Creating Directory " + str(count) + " of " + str(len(directories)))
    if not os.path.exists(path + "\\output\\" + vname + "\\" + directory):
        os.makedirs(path + "\\output\\" + vname + "\\" + directory)
    count = count + 1

#Output Files
print(colors.OKGREEN + "Outputting Files" + colors.ENDC)
count = 1
imagefiles = [f for f in listdir(path + "\\images") if os.path.isfile(os.path.join(path + "\\images", f))]
index = open(path + "\\output\\" + vname + "\\index.txt", "w")
for file in imagefiles:
    print("Outputting Image " + str(count) + " of " + str(len(imagefiles)))
    copyfile(path + "\\images\\" + file, path + "\\output\\" + vname + "\\Image\\" + file)
    index.write(vname + "\tImage\t" + file + "\tOTHER\tOther\tPictures\n")
    count = count + 1
index.close()

#Create Zip File
print(colors.OKBLUE + "Making Zip File" + colors.ENDC)
shutil.make_archive(path + "\\output\\UploadMe", 'zip', path + "\\output\\" + vname)
print(colors.OKGREEN + "Finished" + colors.ENDC)
print(colors.OKGREEN + colors.BOLD + "Images Processed Successfully!" + colors.ENDC)