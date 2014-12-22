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