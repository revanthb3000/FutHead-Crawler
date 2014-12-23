"""
All 'mechanize-related' operations go in here.
"""

import mechanize

baseUrl = "http://www.futhead.com/<FIFAVERSION>/players/<PLAYERID>/"

"""
Set up the required configuration and return a browser to use.
"""
def getBrowserHandler():
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    browser.addheaders = [('User-agent', 'Firefox')]
    return browser

"""
This function returns the player's name and the stats page.
"""
def getPlayerPageContents(browser, fifaVersion, playerId):
    url = baseUrl.replace("<FIFAVERSION>", str(fifaVersion)).replace("<PLAYERID>", str(playerId))
    #TODO: For FIFA 13, the URL is slightly different. Have to look at that.
    browser.open(url)
    pageSource = browser.response().read()
    title = browser.title()
    title = title[0:title.find("FIFA")].strip()
    playerInfo = {"playerName" : title, "futHeadPage" : pageSource}
    return playerInfo