import os
os.getcwd()
collection = "."

def rename(collection, newFilename, startingNumber, extension):
    for i, filename in enumerate(os.listdir(collection)):
        if filename != 'rename.py':
            os.rename(filename, newFilename + str(int(startingNumber) + i) + ('.' + extension)

def menu():
    print("#-----------------------------#RENAMER 1.0#-----------------------------#")
    collection = input("Enter the folder where are located the files you want to rename. If the script is located in the folder, just press enter\n>")
    if collection == None:
        collection = "."
    newFilename = input("Enter the filename you want to give to your files.\n>")
    startingNumber = input("Enter the starting number for the consecutive number of the renamed files.\n>")
    extension = input("Enter the file extension you want your files to have, without the dot\n>")
    rename(collection, newFilename, startingNumber, extension)

menu()