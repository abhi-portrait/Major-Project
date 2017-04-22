#  Created by Harshit Bhat on 13/03/17.
#  Copyright 2017 Harshit Bhat. All rights reserved.

import sys

sys.path.append('/home/abhi/Desktop/Django_Projects/mysite/polls/')

import MySQLdb
from dbConnect import Connect
from SQLHandler import sqlHandler
from getpass import getpass
from faSETS import fasets

# def takeDBCredential():
#     username = raw_input("Enter username of MySQL Database:     ")
#     password = getpass("Enter password of MySQL Database:     ")
#     dbName = raw_input("Enter the name of the database:     ")
#     return username,password,dbName

def takeUserInputs():
    # print
    # print
    # print
    # print
    year = "2011"
    country = "india"
    return year,country

def main():
    username = "root"
    password = ""
    dbName = "Terrorism"
    dbConnector = Connect(username,password,dbName)
    cursor = dbConnector.connectToDb()
    mainAttribute1 = "country_txt"
    mainAttribute2 = "iyear"
    tableName = "attacks"
    attribute1 = "attacktype1_txt"
    attribute2 = "city"
    attribute3 = "targtype1_txt"

    if cursor == None:
        print("There is an error")
    else:
        year,country = takeUserInputs()
        handler = sqlHandler()
        mainQuery = handler.makeCountQueryForTwoAttribute(tableName,mainAttribute1,country,mainAttribute2,year)
        mainQueryCount = handler.getCount(cursor,mainQuery)
        totalCountQuery = handler.getTotalCountQuery(tableName)
        totalCount = handler.getCount(cursor,totalCountQuery)
        topResultsMainQuery = handler.makeQueryForTop50ResultsOnMainQueryThreeAttributes(tableName,attribute1,attribute2,attribute3,mainAttribute1,country,mainAttribute2,year)
        handler.showResults(cursor,topResultsMainQuery,attribute1,attribute2,attribute3)
        ft = fasets()
        finalOneFasetList = list()
        finalOneFasetList = ft.generateTopResultsForThreeAttributes(cursor,handler,tableName,mainQueryCount,totalCount,mainAttribute1,country,mainAttribute2,year,attribute1,attribute2,attribute3)
        return finalOneFasetList
# if __name__ == '__main__':
#     main()
