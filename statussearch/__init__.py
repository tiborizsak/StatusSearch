import os
import re
from glob import iglob
from datetime import datetime

def globsearch(directory):
    for f in iglob(str(directory + '**\\*'), recursive=True):
        return f

class EnhancedFilepath(object): #for experimental purpose => dunder
    def __init__(self, path, extension, filelist=[]):
        self.path = str(path + '**\\*')
        self.extension = extension
        self.filelist = filelist
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index >= len(self.filelist):
            self.index = -1
            raise StopIteration
        elif os.path.isfile(self.filelist[self.index]) and self[-4:] == self.extension:
            return self.filelist[self.index]

class Filepath:
    def __init__(self, path: str, extension: str):
        self.path = str(path + '**\\*')
        self.extension = extension
        self.filelist = []
        for f in iglob(self.path, recursive=True):
            if os.path.isfile(f) and f[-4:] == extension:
                self.filelist.append(f)

class Findstatus:
    def __init__(self, path: str, filelist: list, status: str, outputtxtpath: str):
        self.path = path
        self.filelist = filelist
        self.status = re.compile(status)
        self.outputtxtpath = os.path.join(outputtxtpath)
        for file in self.filelist:
            with open(file) as f:
                read = f.read()
                if self.status.search(read):
                    of = open(self.outputFilePath, 'a')
                    of.write(file + '\n')
                    of.close()

