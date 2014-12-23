import webHandler
import utilityFunctions
import statExtractor

def main():
    browser = webHandler.getBrowserHandler()
    for playerId in range(1,15400):
        getPlayerInfo(browser, 15, playerId)

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
    
    print "Player Name : " + playerName
    playerFileContents = ""
    playerFileContents += "Player Details : \n" + playerDetails + "\n"
    playerFileContents += "Player Rating : " + str(playerRating) + "\n"
    playerFileContents += "Base Stats : \n" + playerBaseStats + "\n"
    playerFileContents += "Individual Stats : \n" + playerIndividualStats + "\n"
    
    fileName = "../data/" + str(fifaVersion) + "/" + str(playerId) + " - " + playerName + ".dat"
    utilityFunctions.writeSourceToFile(fileName, playerFileContents.encode('utf-8'))
    

if __name__ == '__main__':
    main()