import os

# Listing dirs to iterate through for statussearch.findstatus
# Returns list of subdirectories
def listdirstoiterate(directory):
    subdirs = []
    for foldername in os.listdir(directory):
        subdirs.append(foldername)

    return subdirs
