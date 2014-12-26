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
    connection.execute("CREATE INDEX PlayerInfoIndex ON PlayerInfo(pid);")
    
    connection.execute("CREATE TABLE PlayerStats (pid int, PAC int);")
    connection.execute("CREATE INDEX PlayerStatsIndex ON PlayerStats(pid);")
    
    connection.execute("CREATE TABLE GoalkeeperStats (pid int, PAC int);")
    connection.execute("CREATE INDEX GoalkeeperStatsIndex ON PlayerStats(pid);")    
    return

def createFIFADB(fifaVersion):    
    connection = createConnection(fifaVersion)
    createTables(connection, fifaVersion)

def main():
    createFIFADB(15)
    return

if __name__ == '__main__':
    main()