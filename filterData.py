"""
This is a simple quick script to filter the scraped data for FIFA 13 and FIFA 15
"""
import os

def filterData(fifaVersion):
    inputDir = "data/" + str(fifaVersion)
    outputDir = "data/" + str(fifaVersion) + "-filtered"
    for playerFile in os.listdir(inputDir):
        filterFile(inputDir + "/" + playerFile,outputDir + "/" + playerFile)

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
