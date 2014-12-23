"""
All the Parsing and formatting function occur here.
The BS file !
"""

from bs4 import BeautifulSoup
import re

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
    playerRating = soup.findAll('div',{"class":re.compile('^playercard-rating')})
    print playerRating

"""
Gets the player's base stats.
Similar point as stated before. Take only the first six elements to get the base stats and ignore all informs/transfer stats.
"""
def getBaseStats(soup):
    baseStats = soup.findAll('div', {"class":re.compile('^playercard-attr')})
    print baseStats

"""
Each individual stat is obtained here. There's no in-form issue in this case though.
"""
def getIndividualStats(soup):
    playerStats = soup.findAll('div', {"class":re.compile('^attr')})
    print playerStats

def getPlayerDetails():
    return