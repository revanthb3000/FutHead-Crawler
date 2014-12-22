import BeautifulSoup
import webHandler
import utilityFunctions

def main():
    browser = webHandler.getBrowserHandler()
    playerInfo = webHandler.getPlayerPageContents(browser, 15, 1)
    utilityFunctions.writeSourceToFile(playerInfo["playerName"], playerInfo["futHeadPage"])

if __name__ == '__main__':
    main()