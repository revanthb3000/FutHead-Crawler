"""
All frequently used functions/utilities will be written over here.
"""
import webHandler
import statExtractor

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