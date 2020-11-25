import os
import shutil
import zipfile

class Uzip:
    def __init__(self, path: str):
        self.path = path
        for file in os.listdir(self.path):
            fullpath = os.path.join(self.path, file)
            tounzippath = os.path.join(self.path, file[8:16])
            with zipfile.ZipFile(fullpath, "r") as zip_ref:
                zip_ref.extractall(tounzippath)
            os.remove(fullpath)

class Cuttree:
    def __init__(self, path: str, tocut: str, toplace: str):
        self.path = path
        self.tocut = tocut
        self.toplace = toplace
        for folder in os.listdir(path):
            tocopy = os.path.join(self.path, str(folder + self.tocut))
            copydst = os.path.join(self.path, str(folder + self.toplace))
            shutil.copytree(tocopy, copydst)
            shutil.rmtree(os.path.join(self.path, str(folder + '\\C')))
