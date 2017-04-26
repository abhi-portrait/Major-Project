#  Created by Harshit Bhat on 13/03/17.
#  Copyright 2017 Harshit Bhat. All rights reserved.

import sys

sys.path.append('/home/abhi/Desktop/Django_Projects/mysite/polls/')

import MySQLdb
from dbConnect import Connect
from SQLHandler import sqlHandler
from getpass import getpass
from faSETS import fasets
from process import recommendation
from twoFasset import twoFasets
from sys import exit

# def takeDBCredential():
#     username = raw_input("Enter username of MySQL Database:     ")
#     password = getpass("Enter password of MySQL Database:     ")
#     dbName = raw_input("Enter the name of the database:     ")
#     return username,password,dbName
# year = ""
# country = ""

# def takeUserInputs(Year,Country):
#     # print
#     # print
#     # print
#     # print
#     year = Year
#     country = Country
# initialQueryResultList = list()
def checkUserInputs(cursor,handler,tableName,mainAttribute1,country,mainAttribute2,year):
    # query = handler.makeCountQueryForTwoAttribute(tableName,mainAttribute1,country,mainAttribute2,year)
    # queryCount = handler.getCount(cursor,query)
    isValid = True
    # if year<1970 and year>2015:
    #     isValid = False
    # if queryCount == 0:
    #     isValid = False
    return isValid

def mainOneFaset(mainAttribute1,mainAttribute1Val,mainAttribute2,mainAttribute2Val):
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
        # year,country = takeUserInputs("2011","india")
        mainAttribute2Val = mainAttribute2Val
        mainAttribute1Val = mainAttribute1Val
        handler = sqlHandler()
        if checkUserInputs(cursor,handler,tableName,mainAttribute1,mainAttribute1Val,mainAttribute2,mainAttribute2Val) == True:
            mainQuery = handler.makeCountQueryForTwoAttribute(tableName,mainAttribute1,mainAttribute1Val,mainAttribute2,mainAttribute2Val)
            mainQueryCount = handler.getCount(cursor,mainQuery)
            totalCountQuery = handler.getTotalCountQuery(tableName)
            totalCount = handler.getCount(cursor,totalCountQuery)
            topResultsMainQuery = handler.makeQueryForTop50ResultsOnMainQueryThreeAttributesWithTwoMainAttribute(tableName,attribute1,attribute2,attribute3,mainAttribute1,mainAttribute1Val,mainAttribute2,mainAttribute2Val)
            handler.showResults(cursor,topResultsMainQuery,attribute1,attribute2,attribute3)
            ft = fasets()
            global finalOneFasetList

            finalOneFasetList = ft.generateTopResultsForThreeAttributes(cursor,handler,tableName,mainQueryCount,totalCount,mainAttribute1,mainAttribute1Val,mainAttribute2,mainAttribute2Val,attribute1,attribute2,attribute3)
            return finalOneFasetList
        else:
            print ("Invalid1 Input")


def mainTwoFaset(mainAttribute1,mainAttribute1Val,mainAttribute2,mainAttribute2Val):
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
        # year,country = takeUserInputs("2011","india")
        mainAttribute2Val = mainAttribute2Val
        mainAttribute1Val = mainAttribute1Val
        handler = sqlHandler()
        if checkUserInputs(cursor,handler,tableName,mainAttribute1,mainAttribute1Val,mainAttribute2,mainAttribute2Val) == True:
            mainQuery = handler.makeCountQueryForTwoAttribute(tableName,mainAttribute1,mainAttribute1Val,mainAttribute2,mainAttribute2Val)
            mainQueryCount = handler.getCount(cursor,mainQuery)
            totalCountQuery = handler.getTotalCountQuery(tableName)
            totalCount = handler.getCount(cursor,totalCountQuery)
            topResultsMainQuery = handler.makeQueryForTop50ResultsOnMainQueryThreeAttributesWithTwoMainAttribute(tableName,attribute1,attribute2,attribute3,mainAttribute1,mainAttribute1Val,mainAttribute2,mainAttribute2Val)
            # handler.showResults(cursor,topResultsMainQuery,attribute1,attribute2,attribute3)
            twoFt = twoFasets()
            global finalTwoFasetList
            finalTwoFasetList = twoFt.generateTopResultsForThreeAttributes(cursor,handler,tableName,mainQueryCount,totalCount,mainAttribute1,mainAttribute1Val,mainAttribute2,mainAttribute2Val,attribute1,attribute2,attribute3)
            return finalTwoFasetList
        else:
            print ("Invalid3 Input")


def mainRecommend(mainAttribute1,mainAttribute1Val,mainAttribute2,mainAttribute2Val):
    username = "root"
    password = ""
    dbName = "Terrorism"
    dbConnector = Connect(username,password,dbName)
    cursor = dbConnector.connectToDb()
    # mainAttribute1 = "country_txt"
    # mainAttribute2 = "iyear"
    tableName = "attacks"
    attribute1 = "attacktype1_txt"
    attribute2 = "city"
    attribute3 = "targtype1_txt"

    if cursor == None:
        print("There is an error")
    else:
        # year,country = takeUserInputs("2011","india")
        # mainAttribute2Val = mainAttribute2Val
        # mainAttribute1Val = mainAttribute1Val
        handler = sqlHandler()
        if checkUserInputs(cursor,handler,tableName,mainAttribute1,mainAttribute1Val,mainAttribute2,mainAttribute2Val) == True:
            mainQuery = handler.makeCountQueryForTwoAttribute(tableName,mainAttribute1,mainAttribute1Val,mainAttribute2,mainAttribute2Val)
            print(mainAttribute1)
            print(mainAttribute1Val)
            print(mainAttribute2)
            print(mainAttribute2Val)
            print(mainQuery)
            mainQueryCount = handler.getCount(cursor,mainQuery)
            totalCountQuery = handler.getTotalCountQuery(tableName)
            totalCount = handler.getCount(cursor,totalCountQuery)
            recc = recommendation()
            type,attribute1,attribute2,attribute3,mainAttribute1,mainAttribute1Val,mainAttribute2,mainAttribute2Val = recc.moveOn(finalOneFasetList,finalTwoFasetList,mainAttribute1,mainAttribute1Val,mainAttribute2,mainAttribute2Val)
            if mainAttribute2 == "" or mainAttribute2Val == "":
                topResultsMainQuery = handler.makeQueryForTop50ResultsOnMainQueryThreeAttributesWithOneMainAttribute(tableName,attribute1,attribute2,attribute3,mainAttribute1,mainAttribute1Val)
                handler.showResults(cursor,topResultsMainQuery,attribute1,attribute2,attribute3)
                ft = fasets()
                global finalTwoFasetList
                global finalOneFasetList
                finalOneFasetList = ft.generateTopResultsForThreeAttributesWithOneMainAttribute(cursor,handler,tableName,mainQueryCount,totalCount,mainAttribute1,mainAttribute1Val,attribute1,attribute2,attribute3)
                finalTwoFasetList.append("Unable to fetch data")
                # twoFt = twoFasets()
                # twoFasetList = twoFt.generateTopResultsForThreeAttributes(cursor,handler,tableName,mainQueryCount,totalCount,mainAttribute1,mainAttribute1Val,mainAttribute2,mainAttribute2Val,attribute1,attribute2,attribute3)

            else:
                topResultsMainQuery = handler.makeQueryForTop50ResultsOnMainQueryThreeAttributesWithTwoMainAttribute(tableName,attribute1,attribute2,attribute3,mainAttribute1,mainAttribute1Val,mainAttribute2,mainAttribute2Val)
                handler.showResults(cursor,topResultsMainQuery,attribute1,attribute2,attribute3)
                ft = fasets()
                global finalTwoFasetList
                global finalOneFasetList
                finalOneFasetList = ft.generateTopResultsForThreeAttributes(cursor,handler,tableName,mainQueryCount,totalCount,mainAttribute1,mainAttribute1Val,mainAttribute2,mainAttribute2Val,attribute1,attribute2,attribute3)
                # twoFasetList = mfaset.takeUserInputs(mainAttribute2Val,mainAttribute1Val)
                twoFt = twoFasets()
                finalTwoFasetList.clear()
                finalTwoFasetList = twoFt.generateTopResultsForThreeAttributes(cursor,handler,tableName,mainQueryCount,totalCount,mainAttribute1,mainAttribute1Val,mainAttribute2,mainAttribute2Val,attribute1,attribute2,attribute3)
                #recc = recommendation()
                #type,attribute1,attribute2,attribute3,mainAttribute1,mainAttribute1Val,mainAttribute2,mainAttribute2Val = recc.moveOn(oneFasetList,twoFasetList,mainAttribute1,mainAttribute1Val,mainAttribute2,mainAttribute2Val)
        else:
            print ("Invalid2 Input")

# if __name__ == '__main__':
#     main()
