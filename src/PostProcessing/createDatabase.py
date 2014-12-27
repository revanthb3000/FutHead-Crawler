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
                                                "club text, league text, position text," \
                                                "height text, attack_WR text, defense_WR," \
                                                "skills int, weakFoot int, traits text);")
    
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

def createFIFADB(fifaVersion):    
    connection = createConnection(fifaVersion)
    createTables(connection, fifaVersion)

def main():
    createFIFADB(15)
    return

if __name__ == '__main__':
    main()