import os

def uzip(directory):
    for foldername in os.listdir(directory):
        fullpath = os.path.join(directory, foldername)
        tounzipPath = os.path.join(directory, foldername[8:18])
        with zipfile.ZipFile(fullpath, "r") as zip_ref:
            zip_ref.extractall(tounzipPath)
