"""
When the FIFA 12, 13 pages were extracted, the filenames (extracted from the title) were slightly different when compared to FIFA 14,15.
This scripts converts the names into that format.
"""
import os

"""
Takes in a fileName, gets the new fileName and then does the rename.
Example : 1 - Marouane Fellaini 79 rating -.dat gets converted to 1 - Marouane Fellaini.dat
"""
def renameFile(dataDirectory, fileName):
    newFileName = fileName.replace(".dat","").replace("-","")
    splitString = newFileName.split()
    desiredLength = len(splitString) - 2
    newFileName = splitString[0] + " - "
    for i in range(1,desiredLength):
        newFileName += splitString[i] + " "
    newFileName = newFileName.strip() + ".dat"
    os.rename(dataDirectory + fileName, dataDirectory + newFileName)

"""
Iterates through each file and renames it.
"""
def renameFiles(fifaVersion):
    dataDirectory = "data/" + str(fifaVersion) + "/"
    for playerFile in os.listdir(dataDirectory):
        print playerFile
        renameFile(dataDirectory, playerFile)

def main():
    renameFiles(12)
    renameFiles(13)

if __name__ == '__main__':
    main()