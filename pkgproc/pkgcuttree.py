import os
import shutil

def cuttree(directory, datadestination):
    for foldername in os.listdir(directory):
        fullpath = os.path.join(directory, foldername)
        src = os.path.join(directory, foldername + datadestination)
        shutil.copytree(src, fullpath)
