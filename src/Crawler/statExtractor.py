"""
All the Parsing and formatting function occur here.
The BS file !
"""

from bs4 import BeautifulSoup
import re
import utilityFunctions

"""
Just getting a soupHandler once and reusing it for all operations. Don't want to process the sourcecode more than once.
"""
def getSoupHandler(sourceCode):
    soup = BeautifulSoup(sourceCode)
    return soup

"""
Gets the player's overall rating.
A point to note here is that the expected behavior is to get only one matching division. However, you could get multiple elements in the list. Why ? In-forms/Transfers. 
So, only take the first one element for the correct base overall rating.
"""
def getPlayerRating(soup):
    playerRatingElement = soup.findAll('div',{"class":re.compile('^playercard-rating')})
    playerRating = playerRatingElement[0].text
    return playerRating

"""
Gets the player's base stats.
Similar point as stated before. Take only the first six elements to get the base stats and ignore all informs/transfer stats.
"""
def getBaseStats(soup):
    baseStatsElements = soup.findAll('div', {"class":re.compile('^playercard-attr')})
    baseStats = ""
    for i in range(0,6):
        baseStats += baseStatsElements[i].text + "\n"
    return baseStats.strip()

"""
Each individual stat is obtained here. There's no in-form issue in this case though.
"""
def getIndividualStats(soup):
    playerStatsElements = soup.findAll('div', {"class":re.compile('^attr')})
    playerStats = ""
    for stat in playerStatsElements:
        attribute = stat.text
        if(("Rating" in attribute) or ("Stats" in attribute)):
            continue
        else:
            playerStats += attribute.replace("\n"," ").strip() + "\n"
    return playerStats.strip()

"""
This part is a bit tricky. The last entry in the list is expected to be the EA Tax Calculator and can be ignored.
"""
def getPlayerDetails(soup):
    playerDataElements = soup.findAll('table',{"class":"table table-striped table-condensed"})
    playerData = "Full Name "
    playerData += utilityFunctions.scrapeTable(playerDataElements[0]) + "\n"
    playerData += utilityFunctions.scrapeTable(playerDataElements[1])
    return playerData

"""
This function gets the URL of the player's pic.
"""
def getPlayerPicLink(soup):
    picDiv = soup.findAll('div',{"class":"playercard-picture"})[0]
    url = picDiv.findAll('img')[0]['src']
    return url