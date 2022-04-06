import os
os.getcwd()

for filename in enumerate(os.listdir(".")): # for all files in current directory
    if filename != 'renameRV_.py': # avoid renaming the py renamer
        os.rename(filename[1], ("RV_" + filename[1]))