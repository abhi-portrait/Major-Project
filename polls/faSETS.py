#  Created by Harshit Bhat on 09/04/17.
#  Copyright 2017 Harshit Bhat. All rights reserved.

import MySQLdb
from SQLHandler import sqlHandler
import operator

class fasets:

    def giveTopResultsDict(self,cursor,tableName,attribute,mainAttribute1,mainAttribute1Val,mainAttribute2,mainAttribute2Val):
        query = "SELECT " + attribute + " , COUNT(*) as Frequency FROM " + tableName + " where " + mainAttribute1 + " = " + "'" + mainAttribute1Val + "'" + " and " + mainAttribute2 + " = " + "'" + mainAttribute2Val + "'" + " GROUP BY " + attribute + " ORDER BY COUNT(*) DESC LIMIT 5"
        dictType = dict()
        try:
            cursor.execute(query)
            results = cursor.fetchall()
            for i in results:
                key = i[0]
                val = i[1]
                if key != "Unknown":
                    dictType[key] = val
        except:
            print ("Unable to fetch data")

        return dictType

    # def printDicts(self,someDict):
    #     for i in someDict:
    #         print "         " + i + " : ",
    #         print someDict[i]

    # def showDicts(self,dict1,dict2,dict3):
    #     print "     ATTACK TYPE TOP RESULTS:      "
    #     self.printDicts(dict1)
    #
    #     print "     CITY TOP RESULTS:     "
    #     self.printDicts(dict2)
    #
    #     print "     TARGET TYPE TOP RESULTS:      "
    #     self.printDicts(dict3)

    def giveScoreDict(self,cursor,handler,tableName,mainQueryCount,totalCount,anyDict,attribute):
        print('mainquerycount')
        print(mainQueryCount)
        someDict = dict()
        for i in anyDict:
            num = anyDict[i] / (mainQueryCount * 1.0)
            denomNum = handler.getCount(cursor,handler.makeQuery(tableName,attribute,i))
            denom = denomNum / (totalCount * 1.0)
            someDict[i] = num / (denom * 1.0)
        return someDict

    def sortScores(self,dict1,dict2,dict3):
        sortedDict = dict()
        for i in dict1:
            sortedDict[i] = dict1[i]
        for i in dict2:
            sortedDict[i] = dict2[i]
        for i in dict3:
            sortedDict[i] = dict3[i]
        x = sorted(sortedDict.items(),key=operator.itemgetter(1))
        return x

    def calculateScores(self,cursor,handler,tableName,mainQueryCount,totalCount,typeOneDict,typeTwoDict,typeThreeDict,attribute1,attribute2,attribute3):
        typeOneScoreDict = self.giveScoreDict(cursor,handler,tableName,mainQueryCount,totalCount,typeOneDict,attribute1)
        typeTwoScoreDict = self.giveScoreDict(cursor,handler,tableName,mainQueryCount,totalCount,typeTwoDict,attribute2)
        typeThreeScoreDict = self.giveScoreDict(cursor,handler,tableName,mainQueryCount,totalCount,typeThreeDict,attribute3)

        sortedScores = self.sortScores(typeOneScoreDict,typeTwoScoreDict,typeThreeScoreDict)
        return sortedScores

    def maintainList(self,oneFasetList,attribute,someDict):
        for key in someDict:
            s = list()
            s.append(attribute)
            s.append(key)
            oneFasetList.append(s)

    def maintainFinalList(self,someDict,someList):
        for aList in someList:
            parameter = aList[1]
            for tupple in someDict:
                if tupple[0] == parameter:
                    aList.append(tupple[1])
                    break

    def giveTopResultsDictWithOneMainAttribute(self,cursor,tableName,attribute,mainAttribute1,mainAttribute1Val):
        query = "SELECT " + attribute + " , COUNT(*) as Frequency FROM " + tableName + " where " + mainAttribute1 + " = " + "'" + mainAttribute1Val + "'" + " GROUP BY " + attribute + " ORDER BY COUNT(*) DESC LIMIT 5"
        dictType = dict()
        try:
            cursor.execute(query)
            results = cursor.fetchall()
            for i in results:
                key = i[0]
                val = i[1]
                if key != "Unknown":
                    dictType[key] = val
        except:
            print ("Unable to print data")
        return dictType

    def generateTopResultsForThreeAttributesWithOneMainAttribute(self,cursor,handler,tableName,mainQueryCount,totalCount,mainAttribute1,mainAttribute1Val,attribute1,attribute2,attribute3):
        print('mainquerycount')
        print(mainQueryCount)
        typeOneDict = self.giveTopResultsDictWithOneMainAttribute(cursor,tableName,attribute1,mainAttribute1,mainAttribute1Val)
        typeTwoDict = self.giveTopResultsDictWithOneMainAttribute(cursor,tableName,attribute2,mainAttribute1,mainAttribute1Val)
        typeThreeDict = self.giveTopResultsDictWithOneMainAttribute(cursor,tableName,attribute3,mainAttribute1,mainAttribute1Val)
        oneFasetList = list()
        self.maintainList(oneFasetList,attribute1,typeOneDict)
        self.maintainList(oneFasetList,attribute2,typeTwoDict)
        self.maintainList(oneFasetList,attribute3,typeThreeDict)
        scores = self.calculateScores(cursor,handler,tableName,mainQueryCount,totalCount,typeOneDict,typeTwoDict,typeThreeDict,attribute1,attribute2,attribute3)
        self.maintainFinalList(scores,oneFasetList)
        oneFasetList = sorted(oneFasetList,key = operator.itemgetter(2),reverse = True)
        # print "     1 Faset Recommendations     "
        # for i in oneFasetList:
        #     print i
        return oneFasetList




    def generateTopResultsForThreeAttributes(self,cursor,handler,tableName,mainQueryCount,totalCount,mainAttribute1,mainAttribute1Val,mainAttribute2,mainAttribute2Val,attribute1,attribute2,attribute3):
        typeOneDict = self.giveTopResultsDict(cursor,tableName,attribute1,mainAttribute1,mainAttribute1Val,mainAttribute2,mainAttribute2Val)
        typeTwoDict = self.giveTopResultsDict(cursor,tableName,attribute2,mainAttribute1,mainAttribute1Val,mainAttribute2,mainAttribute2Val)
        typeThreeDict = self.giveTopResultsDict(cursor,tableName,attribute3,mainAttribute1,mainAttribute1Val,mainAttribute2,mainAttribute2Val)
        oneFasetList = list()
        self.maintainList(oneFasetList,attribute1,typeOneDict)
        self.maintainList(oneFasetList,attribute2,typeTwoDict)
        self.maintainList(oneFasetList,attribute3,typeThreeDict)
        #self.showDicts(typeOneDict,typeTwoDict,typeThreeDict)
        scores = self.calculateScores(cursor,handler,tableName,mainQueryCount,totalCount,typeOneDict,typeTwoDict,typeThreeDict,attribute1,attribute2,attribute3)
        self.maintainFinalList(scores,oneFasetList)
        oneFasetList = sorted(oneFasetList,key = operator.itemgetter(2),reverse = True)
        return oneFasetList
