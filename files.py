import os
from os import listdir
def GetDirectorySize(path):
    size = 0
    onlyfiles = [f for f in listdir(path) if os.path.isfile(os.path.join(path, f))]
    for file in onlyfiles:
        size = size + os.path.getsize(path + "\\" + file)
    kilobytes = size / 1024
    megabytes = kilobytes / 1024
    return megabytes
