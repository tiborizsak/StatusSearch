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

searchlist = globsearch(directory)

efp = EnhancedFilepath(directory, extension, searchlist) # exprimental not working yet

counter = 0

for e in efp:
    counter += 1
    print(e)
    print(counter)
