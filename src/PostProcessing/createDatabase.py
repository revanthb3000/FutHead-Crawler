"""
This script will take in all these extracted data files and put them into an sqlite3 database.
"""
import sqlite3
import os

"""
This function returns a connection to play with.
"""
def createConnection(fifaVersion):
    try:
        #If the DB file is already there, get rid of it.
        os.remove(str(fifaVersion) + ".db")
    except:
        None

    connection = sqlite3.connect(str(fifaVersion) + ".db")
    return connection

"""
Creates all the required tables.
"""
def createTables(connection, fifaVersion):
    #Creating the player info tables.
    connection.execute("CREATE TABLE PlayerInfo (pid int, name text, full_name text," \
                                                "club text, league text, nation text, position text," \
                                                "height text, Foot text, attack_WR text, defense_WR," \
                                                "skills int, weak_foot int, traits text);")
    
    #36 entries.
    connection.execute("CREATE TABLE PlayerStats (pid int, PAC int, SHO int, "\
                                                  "PAS int, DRI int, DEF int,"\
                                                  "PHY int, Ball Control int, Crossing int,"\
                                                  "Curve int, Dribbling int, Finishing int,"\
                                                  "Free_Kick_Accuracy int, Heading_Accuracy int, Long_Passing int,"\
                                                  "Long_Shots int, Marking int, Penalties int,"\
                                                  "Short_Passing int, Shot_Power int, Sliding_Tackle int,"\
                                                  "Standing_Tackle int, Volleys int, Acceleration int,"\
                                                  "Agility int, Balance int, Jumping int,"\
                                                  "Reactions int, Sprint_Speed int, Stamina int,"\
                                                  "Strength int, Aggression int, Positioning int,"\
                                                  "Interceptions int, Vision int, Player_Rating int);")
    
    connection.execute("CREATE TABLE GoalkeeperStats (pid int, DIV int, HAN int, "\
                                                     "KIC int, REF int, SPE int,"\
                                                     "POS int, Player_Rating int);")

"""
Important Note : Create Indices AFTER inserting data.
"""
def createIndices(connection):
    connection.execute("CREATE INDEX PlayerInfoIndex ON PlayerInfo(pid);")
    
    connection.execute("CREATE INDEX PlayerStatsIndex ON PlayerStats(pid);")
    
    connection.execute("CREATE INDEX GoalkeeperStatsIndex ON GoalkeeperStats(pid);")

"""
This function will process the data files and insert that data into the database.
"""
def processFile(dataDirectory, fileName, fifaVersion):
    splitString = fileName.replace(".dat","").split("-")
    playerId = int(splitString[0].strip())
    playerName = splitString[1].strip()
    playerInfoFields = ["Full Name", "Club","League","Nation","Position",
                        "Height","Foot","Attack Workrate","Defensive Workrate",
                        "Weak Foot", "Skill Moves", "Traits", "Player Rating"]
    
    #The HEA attribute was replaced with PHY from FIFA 15 onwards.
    finalBaseAttribute = "HEA"
    if(fifaVersion == 15):
        finalBaseAttribute = "PHY"
        
    playerStatsFields = ["PAC","SHO","PAS","DRI",
                         "DEF",finalBaseAttribute,"Ball Control", "Crossing", 
                         "Curve", "Dribbling", "Finishing", "Free Kick Accuracy", 
                         "Heading Accuracy", "Long Passing", "Long Shots", "Marking", 
                         "Penalties", "Short Passing", "Shot Power", "Sliding Tackle", 
                         "Standing Tackle", "Volleys", "Acceleration", "Agility", 
                         "Balance", "Jumping", "Reactions", "Sprint Speed", 
                         "Stamina", "Strength", "Aggression", "Positioning", 
                         "Interceptions", "Vision"]

    GKStatsFields = ["DIV", "HAN", "KIC",
                     "REF", "SPE", "POS"]


    playerInfo = {}
    playerStats = {}
    
    
    fileHandle = open(dataDirectory + fileName,"r")
    lines = fileHandle.readlines()
    fileHandle.close()
    
    for line in lines:
#         print line,
        for field in playerInfoFields:
            if(line.find(field)==0):
                playerInfo[field] = line.replace(field,"").strip()

    playerAttributes = playerStatsFields
    isGoalKeeper = False
    if(playerInfo["Position"]=="GK"):
        isGoalKeeper = True
        playerAttributes = GKStatsFields
    
    for line in lines:
        line = line.strip()
        split = line.find(" ")
        value = line[0:split]
        field = line[(split+1):]
        if(field in playerAttributes):
            playerStats[field] = int(value)

    print "Is GoalKeeper ? " + str(isGoalKeeper)
    print playerId
    print playerName
    print playerInfo    
    print playerStats

def createFIFADB(fifaVersion):    
#     connection = createConnection(fifaVersion)
#     createTables(connection, fifaVersion)
    dataDirectory = "data/" + str(fifaVersion)
    if(fifaVersion==12 or fifaVersion==13):
        dataDirectory += "-filtered"
    dataDirectory += "/"
    for playerFile in os.listdir(dataDirectory):
        print playerFile
        processFile(dataDirectory, playerFile, fifaVersion)
        break
    processFile(dataDirectory, "4 - Casillas.dat", fifaVersion)

def main():
    createFIFADB(15)
    return

if __name__ == '__main__':
    main()