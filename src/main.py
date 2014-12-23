import webHandler
import utilityFunctions
import statExtractor

def main():
    browser = webHandler.getBrowserHandler()
    getPlayerInfo(browser, 14, 2)

def getPlayerInfo(browser, fifaVersion, playerId):
    playerInfo = webHandler.getPlayerPageContents(browser, fifaVersion, playerId)
    soup = statExtractor.getSoupHandler(playerInfo["futHeadPage"])
    
    print "Player Rating : "
    statExtractor.getPlayerRating(soup)
    
    print "Base Stats : "
    statExtractor.getBaseStats(soup)
    
    print "Individual Stats : "
    statExtractor.getIndividualStats(soup)
    
    utilityFunctions.writeSourceToFile(playerInfo["playerName"], playerInfo["futHeadPage"])
    

if __name__ == '__main__':
    main()