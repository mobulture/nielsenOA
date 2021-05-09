import DBwork
import csv

#Used for populating the database, it is already populated so no need to run
createdb = "CREATE DATABASE shows"
create_shows = "CREATE TABLE IF NOT EXISTS Show (title TEXT , studio TEXT, location TEXT, genre TEXT, viewers INTEGER ,PRIMARY KEY(title,studio,location));"

create_genre = "CREATE TABLE IF NOT EXISTS Genre (title TEXT , studio TEXT, genre TEXT,PRIMARY KEY(title,studio,genre))"


DBwork.dbInsert(create_genre)
csvPath = "ShowData.csv"
def parseCsv(csvPath):
    allRows=[]
    with open(csvPath) as csvFile :
        csvRead = csv.DictReader(csvFile)
        for rows in csvRead:
            newRow = {}
            for key,item in rows.items():
                if key.startswith("ï»¿P"):
                    key = key[3:]
                newRow[key] = item
            allRows.append(newRow)
    return allRows
DBwork.dbInsert(createdb)
DBwork.dbInsert(create_shows)
DBwork.dbInsert(create_genre)

def insertShow(show):
    showQuery = "INSERT into show (title,studio,location,genre,viewers) values ('%s','%s','%s','%s','%s')" % (show["Program Title"], show["Program Network"], show["Viewer Hometown"], show["Program Genre"], show["Number of Viewers"])
    DBwork.dbInsert(showQuery)

showData = parseCsv(csvPath)
for show in showData:
    insertShow(show)
