
# StatusSearch
This program is dedicated to quickly find several type of device status through a vast amount of logfiles. Prior the search the data batches coming from each device need to be processed. I use os glob shutil and zipfile modules to unzip handle folders/files. For search I use regular expressions to compile them re package gives me a hand. The main purpose of this project were driven by the demand to find a fast solution for running through large amount of files so it is not yet full-proof and need to be run with manual intervention.
##pkgproc
```python
class Uzip:
    def __init__(self, path: str):
        self.path = path
        for file in os.listdir(self.path):
            fullpath = os.path.join(self.path, file)
            tounzippath = os.path.join(self.path, file[8:16])
            with zipfile.ZipFile(fullpath, "r") as zip_ref:
                zip_ref.extractall(tounzippath)
            os.remove(fullpath)
```
The name of the archive contains the id of the device with some other data so it is sliced and the data extracted in the correlating folder. Original archive is removed afterwards.
```python
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
```
The platform where the original zips gathered compress the requested files in the original path where those located on the device. As it is inevitable to open manually the outputted files after the run of the app the user can define the folder where to move the files.
##statussearch
Retrieves a file list of a certain user defined extension
```python
class Filepath:
    def __init__(self, path: str, extension: str):
        self.path = str(path + '**\\*')
        self.extension = extension
        self.filelist = []
        for f in iglob(self.path, recursive=True):
            if os.path.isfile(f) and f[-4:] == extension:
                self.filelist.append(f)
```
This class looks up the status and writes the full path of the file in an output file.
```python
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
```
## main
Directory extension and status regexp definition.
```python
from pkgproc import Uzip, Cuttree
from statussearch import Filepath, Findstatus, EnhancedFilepath, globsearch

directory = 'T:\\T\\IWP\\py\\StatusSearch_archive\\DatArc\\'
extension = '.dat'
tocutdst = '\\C\\DatArc\\'
toplacedst = '\\DatArc\\'
outputlist = '\\StatusSearch_archive\\DatArc\\'

statusdivfullre = r'CI01:(3F:60:00|3A:39:39)'
statusfullre = r'003D901:3F:(31|32):(30|31|32|33|34|37|38|39|)'
statusemptyre = r'003D902:3F:(31|32):(30|31|32|33|34|37|38|39|)'
statuslowre = r'003D902:2D:'

u = Uzip(directory)
c = Cuttree(directory, tocutdst, toplacedst)
f = Filepath(directory, extension)
s = Findstatus(directory, f.filelist, statuslowre, outputlist)
```
## dunder method
Experiment to use magic to make a custom iterator class with __init__, __next__ and __iter__ methods.
```python
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
```