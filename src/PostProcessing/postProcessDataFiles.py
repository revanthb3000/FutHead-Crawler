"""
This is a simple quick script to filter the scraped data for FIFA 13 and FIFA 12
The cost of player cards for various platforms was part of the play info divison and that's creeped into these data files.
"""
import os

def filterData(fifaVersion):
    inputDir = "data/" + str(fifaVersion)
    outputDir = "data/" + str(fifaVersion) + "-filtered"
    for playerFile in os.listdir(inputDir):
        #An important point to be noted here is that few files could have foreign names. Windows seems to be struggling with that.
        print playerFile
        filterFile(inputDir + "/" + playerFile,outputDir + "/" + playerFile)

"""
This gets rid of the player prices on various platforms and converts the existing files to something similar to FIFA 14 and 15
Stuff like this:

Line # | Content
--------------------
2      |Full Name PS3 193,071
3      |Xbox 148,087
4      |PC 295,509
5      |Wayne Rooney
6      |Club Manchester United
7      |League Barclays PL
--------------------

Lines 2,3,4,5 need to be merged into one line - 'Full Name Wayne Rooney'
"""
def filterFile(inputFileName, outputFileName):
    lines = []
    reader = open(inputFileName,"r")
    cnt = 1
    for line in reader.readlines():
        if((cnt >= 2) and (cnt<=4)):
            cnt += 1
            continue
        elif(cnt == 5):
            line = "Full Name " + line
        cnt += 1
        lines.append(line)
    reader.close()

    writer = open(outputFileName,"w")
    for line in lines:
        writer.write(line)
    writer.close()

def main():
    filterData(12)
    filterData(13)

if __name__ == '__main__':
    main()
