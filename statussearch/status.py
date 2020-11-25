
def findstatus(subdirectory):
    sumfilePath = os.path.join(directory, "sumfile.txt")
    for filename in subdirectory:
        tbcfilepath = os.path.join(subdir, filename)
        if filename.endswith(".txt"):
            with open(tbcfilepath) as f:
                if "CI01:3F:60:00" in f.read():
                    sumfile = open(sumfilePath, "a")
                    sumfile.write(tbcfilepath + " - " + "CI01:3F:60:00\n")
                    sumfile.close()
                else:
                    # if "DI02:3D:37:38" and "D902:3D:37:38" in f.read():
                    #     sumfile = open(sumfilePath, "a")
                    #     sumfile.write(filename + " - " + "D902:3D:37:38 and DI02:3D:37:38 - BOTH\n")
                    #     sumfile.close()
                    pass
        else:
            pass