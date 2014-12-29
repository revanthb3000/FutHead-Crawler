"""
All frequently used functions/utilities will be written over here.
"""

"""
Simple function.Give me a filename and contents and this function will do the writing.
"""
def writeSourceToFile(fileName, content):
    fileHandle = open(fileName, "w")
    fileHandle.write(content)
    fileHandle.close()

"""
Given a table element, this function extracts stuff in a readable format.
"""
def scrapeTable(tableElement):
    scrapedTable = ""
    rows = tableElement.findAll('tr')
    for row in rows:
        cols = row.findAll('td')
        attribute = ""
        for col in cols:
            attribute += col.text.strip() + " "
        if(attribute.strip()==""):
            continue
        scrapedTable += attribute.strip() + "\n"
    return scrapedTable.strip()

"""
Given a browser, fifaVersion, playerId and image Url, this function downloads that image and saves it as the filename as constructed from the arguments.
"""
def saveImageToFile(browser, fifaVersion, playerId, imageUrl):
    data = browser.open(imageUrl).read()
    fileName = "pics/" + str(fifaVersion) + "/" + str(playerId) + ".png"
    fileHandle = open(fileName, 'wb')
    fileHandle.write(data)
    fileHandle.close()