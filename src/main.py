import webHandler
import utilityFunctions
import statExtractor
from multiprocessing import Process

def main():
    start = 1
    end = 50000
    cnt = start
    #Number of players crawled per thread.
    numOfPlayers = 5000
    processes = []
    while(cnt < end):
        p = Process(target=crawlPlayerPages,args=(cnt, cnt + numOfPlayers))
        p.start()
        processes.append(p)
        cnt += numOfPlayers

    for process in processes:
        process.join()

"""
Runs the getPlayerInfo function in a loop.
"""            
def crawlPlayerPages(startId, endId):
    browser = webHandler.getBrowserHandler()
    for playerId in range(startId,endId):
        try:
            getPlayerInfo(browser, 12, playerId)
        except:
            print ""

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
    
    fileName = "../data/" + str(fifaVersion) + "/" + str(playerId) + " - " + playerName + ".dat"
    utilityFunctions.writeSourceToFile(fileName, playerFileContents.encode('utf-8'))
    

if __name__ == '__main__':
    main()