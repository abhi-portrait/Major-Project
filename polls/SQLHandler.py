#  Created by Harshit Bhat on 13/03/17.
#  Copyright 2017 Harshit Bhat. All rights reserved.

import MySQLdb
from dbConnect import Connect

class sqlHandler:
    queryResultList = list()
    def makeQuery(self,tableName,attribute,attributeVal):
        s = "SELECT COUNT(*) FROM " + tableName + " where " + attribute + " = '" + attributeVal + "'"
        return s

    def showResults(self,cursor,query,attribute1,attribute2,attribute3):
        try:
            cursor.execute(query)
            results = cursor.fetchall()
            tempList = list()
            tempList.append(attribute1)
            tempList.append(attribute2)
            tempList.append(attribute3)
            self.queryResultList.append(tempList)
            # print "     *****************************************************************************************"
            # print "     [ " + attribute1 + "," + attribute2 + "," + attribute3 + " ]"
            # print "     *****************************************************************************************"
            for i in results:
                tList = list()
                a = i[0]
                b = i[1]
                c = i[2]
                tList.append(a)
                tList.append(b)
                tList.append(c)
                self.queryResultList.append(tList)
                # print "     [ " + a + "," + b + "," + c + " ]"
        except:
            print ("There was an error in retrieving data")
        # print "     *****************************************************************************************"

    def getTotalCountQuery(self,tableName):
        qry = "SELECT COUNT(*) FROM " + tableName
        return qry

    def makeCountQueryForOneAttribute(self,tableName,attribute,attributeVal):
        qry = "SELECT COUNT(*) FROM " + tableName + " WHERE " + attribute + " = " + "'" + attributeVal + "'"
        return qry

    def makeCountQueryForTwoAttribute(self,tableName,attribute1,attribute1Val,attribute2,attribute2Val):
        qry = "SELECT COUNT(*) FROM " + tableName + " WHERE " + attribute1 + " = " + "'" + attribute1Val + "'" + " and " + attribute2 + " = " + "'" + attribute2Val + "'"
        return qry

    def makeQueryForTop50ResultsOnMainQueryThreeAttributes(self,tableName,attribute1,attribute2,attribute3,mainAttribute1,mainAttribute1Val,mainAttribute2,mainAttribute2Val):
        qry = "SELECT " + attribute1 + "," + attribute2 + "," + attribute3 + " from " + tableName + " where " + mainAttribute1 + " = " + "'" + mainAttribute1Val + "'" + " and " + mainAttribute2 + " = " + "'" + mainAttribute2Val + "'" + " LIMIT 50 "
        return qry

    def getCount(self,cursor,query):
        queryCount = 0
        try:
            cursor.execute(query)
            results = cursor.fetchall()
            queryCount = results[0][0]
        except:
            print ("Unable to fetch data")
        return queryCount
