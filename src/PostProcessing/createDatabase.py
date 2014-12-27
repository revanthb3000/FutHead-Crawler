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
    connection.text_factory = str
    return connection

"""
Creates all the required tables.
"""
def createTables(connection, fifaVersion):
    #Creating the player info tables.
    connection.execute("CREATE TABLE PlayerInfo (pid int, name text, full_name text," \
                                                "club text, league text, nation text, position text," \
                                                "height text, Foot text, attack_WR text, defense_WR text," \
                                                "skills int, weak_foot int, traits text);")
    
    #36 entries.
    #The HEA attribute was replaced with PHY from FIFA 15 onwards.
    finalBaseAttribute = "HEA"
    if(fifaVersion == 15):
        finalBaseAttribute = "PHY"
    connection.execute("CREATE TABLE PlayerStats (pid int, PAC int, SHO int, "\
                                                  "PAS int, DRI int, DEF int,"\
                                                  "" + finalBaseAttribute + " int, Ball_Control int, Crossing int,"\
                                                  "Curve int, Dribbling int, Finishing int,"\
                                                  "Free_Kick_Accuracy int, Heading_Accuracy int, Long_Passing int,"\
                                                  "Long_Shots int, Marking int, Penalties int,"\
                                                  "Short_Passing int, Shot_Power int, Sliding_Tackle int,"\
                                                  "Standing_Tackle int, Volleys int, Acceleration int,"\
                                                  "Agility int, Balance int, Jumping int,"\
                                                  "Reactions int, Sprint_Speed int, Stamina int,"\
                                                  "Strength int, Aggression int, Positioning int,"\
                                                  "Interceptions int, Vision int, Player_Rating int);")
    
    #Important point - GK_DIV is used since DIV is an sql keyword.
    connection.execute("CREATE TABLE GoalkeeperStats (pid int, GK_DIV int, HAN int, "\
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
Inserts player details into the PlayerInfo table.
"""
def insertPlayerInfo(cursor, playerId, playerName, playerInfo):
    data = (playerId,playerName,playerInfo["Full Name"],playerInfo["Club"],playerInfo["League"],playerInfo["Nation"],playerInfo["Position"],
         playerInfo["Height"],playerInfo["Foot"],playerInfo["Attack Workrate"],playerInfo["Defensive Workrate"],int(playerInfo["Skill Moves"]),
         int(playerInfo["Weak Foot"]),playerInfo["Traits"])
    cursor.execute("INSERT INTO `PlayerInfo`(`pid`, `name`, `full_name`, `club`, `league`, `nation`, `position`, "\
                                    "`height`, `Foot`, `attack_WR`, `defense_WR`, `skills`, `weak_foot`, `traits`) "\
                                    "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?);", data)

"""
This is used for outfield players. Stats are inserted into the PlayerStats table
"""
def insertPlayerStats(cursor, playerId, playerStats, fifaVersion):
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
                         "Interceptions", "Vision", "Player Rating"]
    data = (playerId,)
    for field in playerStatsFields:
        data += (playerStats[field],)
    print data
    cursor.execute("INSERT INTO `PlayerStats`(`pid`, `PAC`, `SHO`, `PAS`, `DRI`, `DEF`, `"+finalBaseAttribute+"`, "\
                                            "`Ball_Control`, `Crossing`, `Curve`, `Dribbling`, `Finishing`, `Free_Kick_Accuracy`, "\
                                            "`Heading_Accuracy`, `Long_Passing`, `Long_Shots`, `Marking`, `Penalties`, `Short_Passing`, "\
                                            "`Shot_Power`, `Sliding_Tackle`, `Standing_Tackle`, `Volleys`, `Acceleration`, `Agility`, `Balance`, "\
                                            "`Jumping`, `Reactions`, `Sprint_Speed`, `Stamina`, `Strength`, `Aggression`, `Positioning`, `Interceptions`, "\
                                            "`Vision`, `Player_Rating`) "\
                                            "VALUES (?,?,?,?,?,?,?,?,?,"\
                                            "?,?,?,?,?,?,?,?,?,"\
                                            "?,?,?,?,?,?,?,?,?,"\
                                            "?,?,?,?,?,?,?,?,?)", data)

"""
This is used for goalkeepers. Stats are inserted into the GoalkeeperStats table.
"""
def insertGKStats(connection, playerId, playerStats):
    return

"""
This function will process the data files and insert that data into the database.
"""
def processFile(cursor, dataDirectory, fileName, fifaVersion):
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

    #Putting the overall rating in the player Stats dictionary. Why am I using the replace operator ? Because the delimiter for player rating is actually : and not <space>
    playerStats["Player Rating"] = int(playerInfo["Player Rating"].replace(":","").strip())
    
#     print "Is GoalKeeper ? " + str(isGoalKeeper)
#     print playerId
#     print playerName
#     print playerInfo    
#     print playerStats
    
    insertPlayerInfo(cursor, playerId, playerName, playerInfo)
    if(isGoalKeeper):
        insertGKStats(cursor, playerId, playerStats)
    else:
        insertPlayerStats(cursor, playerId, playerStats, fifaVersion)

def createFIFADB(fifaVersion):
    connection = createConnection(fifaVersion)
    createTables(connection, fifaVersion)
    cursor = connection.cursor()
    dataDirectory = "data/" + str(fifaVersion)
    if(fifaVersion==12 or fifaVersion==13):
        dataDirectory += "-filtered"
    dataDirectory += "/"
    for playerFile in os.listdir(dataDirectory):
        print playerFile
        processFile(cursor, dataDirectory, playerFile, fifaVersion)
        break
    processFile(cursor, dataDirectory, "4 - Casillas.dat", fifaVersion)
    createIndices(connection)
    connection.commit()
    connection.close()

def main():
    createFIFADB(15)
    return

if __name__ == '__main__':
    main()