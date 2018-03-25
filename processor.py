import easygui
import os
from os import listdir
from shutil import copyfile
from color import colors
import shutil
import files

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

#Copy all the images to /images and split into 150 mb chunks
print(colors.OKGREEN + "Copying Images" + colors.ENDC)
#Get listing of all files
onlyfiles = [f for f in listdir(path) if os.path.isfile(os.path.join(path, f))]
folderCount = 1
count = 1
#Make the first chunk directory
if not os.path.exists(path + "\\images\\1"):
    os.makedirs(path + "\\images\\1")
for file in onlyfiles:
    print("Copying File " + str(count) + " of " + str(len(onlyfiles)))
    filename = file.split(".")
    suffix = filename[len(filename) - 1]
    if suffix.lower() == "jpg":
        #check if the folder is over 150 megabytes
        if files.GetDirectorySize(path + "\\images\\" + str(folderCount)) >= 150:
            folderCount = folderCount + 1
            #make the new folder
            if not os.path.exists(path + "\\images\\" + str(folderCount)):
                os.makedirs(path + "\\images\\" + str(folderCount))
        copyfile(path + "\\" + file, path + "\\images\\" + str(folderCount) + "\\img" + str(count) + ".jpg")
        os.remove(path + "\\" + file)
    else:
        print(colors.FAIL + file + " skipped due to unsupported format." + colors.ENDC)
        copyfile(path + "\\" + file, path + "\\error\\" + file)
        os.remove(path + "\\" + file)
    count = count + 1

folders = [f for f in listdir(path + "\\images") if os.path.isdir(os.path.join(path + "\\images", f))]
fcount = 1
for folder in folders:
    # Generate Output Directories
    print(colors.OKGREEN + "Outputting Chunk " + str(fcount) + " of " + str(len(folders)) + colors.ENDC)
    print(colors.OKGREEN + "Making Output Directories" + colors.ENDC)
    directories = ["Image"]
    count = 1
    print("Creating Directory " + str(count) + " of " + str(len(directories)))
    #Make volume folder
    if not os.path.exists(path + "\\output\\" + folder + "\\" + vname):
        os.makedirs(path + "\\output\\" + folder + "\\" + vname)
        count = count + 1
    #Make all the rest of the folders
    for directory in directories:
        print("Creating Directory " + str(count) + " of " + str(len(directories)))
        if not os.path.exists(path + "\\output\\" + folder + "\\" + vname + "\\" + directory):
            os.makedirs(path + "\\output\\" + folder + "\\" + vname + "\\" + directory)
        count = count + 1

    # Output Files
    print(colors.OKGREEN + "Outputting Files" + colors.ENDC)
    count = 1
    imageFiles = [f for f in listdir(path + "\\images\\" + folder) if os.path.isfile(os.path.join(path + "\\images\\" + folder, f))]
    index = open(path + "\\output\\" + folder + "\\" + vname + "\\index.txt", "w")
    for file in imageFiles:
        print("Outputting Image " + str(count) + " of " + str(len(imageFiles)))
        copyfile(path + "\\images\\" + folder + "\\" + file, path + "\\output\\" + folder + "\\" + vname + "\\Image\\" + file)
        index.write(vname + "\tImage\t" + file + "\tOTHER\tOther\tPictures\n")
        count = count + 1
    index.close()

    # Create Zip File
    print(colors.OKBLUE + "Making Zip File" + colors.ENDC)
    shutil.make_archive(path + "\\OutputChunk" + folder, 'zip', path + "\\output\\" + folder + "\\" + vname)
    print(colors.OKGREEN + "Finished" + colors.ENDC)
    fcount = fcount + 1
print(colors.OKGREEN + colors.BOLD + "Images Processed Successfully!" + colors.ENDC)
