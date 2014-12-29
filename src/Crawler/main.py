import webHandler
import utilityFunctions
import statExtractor
import sys
from multiprocessing import Process

def main():
    action = sys.argv[1]
    if(action == "pics"):
        getFIFAPics(15)
        getFIFAPics(14)
        getFIFAPics(13)
        getFIFAPics(12)
    else:
        getFIFAData(12)
        getFIFAData(13)
        getFIFAData(14)
        getFIFAData(15)
        
"""
Extracts all data for a given FIFA version.
"""
def getFIFAData(fifaVersion):
    start = 1
    end = 50000
    cnt = start
    #Number of players crawled per thread.
    numOfPlayers = 5000
    processes = []
    while(cnt < end):
        p = Process(target=crawlPlayerPages,args=(cnt, cnt + numOfPlayers, fifaVersion))
        p.start()
        processes.append(p)
        cnt += numOfPlayers

    for process in processes:
        process.join()
        
"""
Extracts all pics for a given FIFA version.
"""
def getFIFAPics(fifaVersion):
    start = 1
    end = 50000
    cnt = start
    #Number of players crawled per thread.
    numOfPlayers = 5000
    processes = []
    while(cnt < end):
        p = Process(target=getPlayerPictures,args=(cnt, cnt + numOfPlayers, fifaVersion))
        p.start()
        processes.append(p)
        cnt += numOfPlayers

    for process in processes:
        process.join()

"""
Runs the getPlayerInfo function in a loop.
"""            
def crawlPlayerPages(startId, endId, fifaVersion):
    browser = webHandler.getBrowserHandler()
    for playerId in range(startId,endId):
        try:
            getPlayerInfo(browser, fifaVersion, playerId)
        except:
            print ""
    browser.close()

"""
This function downloads all player pics
"""  
def getPlayerPictures(startId, endId, fifaVersion):
    browser = webHandler.getBrowserHandler()
    for playerId in range(startId,endId):
        try:
            extractPlayerPicture(browser, fifaVersion, playerId)
        except:
            print ""
    browser.close()

"""
Given a playerId and FIFA version, this function downloads and saves the player's card picture.
It's the div with class= "playercard-picture"
"""
def extractPlayerPicture(browser, fifaVersion, playerId):
    print "Now extracting : " + str(playerId)
    playerInfo = webHandler.getPlayerPageContents(browser, fifaVersion, playerId)
    soup = statExtractor.getSoupHandler(playerInfo["futHeadPage"])
    imageUrl = statExtractor.getPlayerPicLink(soup)
    utilityFunctions.saveImageToFile(browser, fifaVersion, playerId, imageUrl)

"""
This is the main function that stitches all pieces together and writes data to a file.
"""
def getPlayerInfo(browser, fifaVersion, playerId):
    playerInfo = webHandler.getPlayerPageContents(browser, fifaVersion, playerId)
    soup = statExtractor.getSoupHandler(playerInfo["futHeadPage"])
    
    playerName = playerInfo["playerName"]
    playerDetails = statExtractor.getPlayerDetails(soup)
    playerRating = statExtractor.getPlayerRating(soup)
    playerBaseStats = statExtractor.getBaseStats(soup)
    playerIndividualStats = statExtractor.getIndividualStats(soup)
    
    print "Player Name : " + str(playerId) + " - " + playerName
    playerFileContents = ""
    playerFileContents += "Player Details : \n" + playerDetails + "\n"
    playerFileContents += "Player Rating : " + str(playerRating) + "\n"
    playerFileContents += "Base Stats : \n" + playerBaseStats + "\n"
    playerFileContents += "Individual Stats : \n" + playerIndividualStats + "\n"
    
    fileName = "data/" + str(fifaVersion) + "/" + str(playerId) + " - " + playerName + ".dat"
    utilityFunctions.writeSourceToFile(fileName, playerFileContents.encode('utf-8'))
    

if __name__ == '__main__':
    main()