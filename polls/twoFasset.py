import sys

sys.path.append('/home/abhi/Desktop/Django_Projects/mysite/polls/')
import MySQLdb
import operator
from operator import itemgetter
from SQLHandler import sqlHandler
class twoFasets:

    def getCount(self,query):
        db = MySQLdb.connect("127.0.0.1","root","","Terrorism")
        cursor = db.cursor()
        c = 0
        try:
            cursor.execute(query)
            res = cursor.fetchall()
            c = res[0][0]
        except:
            print ("Unable to fetch data 5")

        return c

    def makeQuery(self,attribute1,attributeVal1,attribute2,attributeVal2):
        s = "SELECT COUNT(*) FROM attacks where " + attribute1 + " = '" + attributeVal1 + "' and " + attribute2 + " = '" + attributeVal2 + "' "
        return s

    def giveScoreSortedList(self,someList,totalCount,mainQueryCount):

        if totalCount == 0 or mainQueryCount == 0:
            sortedTwoFacetList = list()
            sortedTwoFacetList.append("Unable to fetch data 3")
            return sortedTwoFacetList
        someListLen = len(someList)
        for i in range(0,someListLen):
            num = someList[i][4] / (mainQueryCount * 1.0)
            denomNum = self.getCount(self.makeQuery(someList[i][0],someList[i][2],someList[i][1],someList[i][3]))
            denom = denomNum / (totalCount * 1.0)
            if denom != 0:
                score = num / (denom * 1.0)
                someList[i].append(score)
        tempList = list()
        for i in range(0,someListLen):
            if someList[i][4] != 0:
                tempList.append(someList[i])
        sortedTwoFacetList = sorted(tempList,key=itemgetter(5),reverse = True)
        return sortedTwoFacetList


    def giveTopResultsList(self,cursor,tableName,attribute,mainAttribute1,mainAttribute1Val,mainAttribute2,mainAttribute2Val):
        query = "SELECT " + attribute + ", COUNT(*) AS FREQUENCY FROM " + tableName + " WHERE " +  mainAttribute1 + " = " + "'" + mainAttribute1Val + "'" + " and " + mainAttribute2 + " = " + "'" + mainAttribute2Val + "'" + " GROUP BY " + attribute + " ORDER BY COUNT(*) DESC LIMIT 5"
        # print query
        listType = list()
        try:
            cursor.execute(query)
            res = cursor.fetchall()
            for i in res:
                a = attribute
                b = i[0]
                if b != "Unknown":
                    listType.append(a)
                    listType.append(b)
        except:
            print ("Unable to fetch data 2")
        return listType

    def  initialTwoFacetList(self,attackList,cityList,targetList):
        initialList = list()
        # if len(attackList)<3 or len(cityList)<3 or len(targetList)<3 :
        #     initialList.append("Unable to fetch data")
        #     return initialList
        attr1Len = len(attackList)
        attr2Len = len(cityList)
        attr3Len = len(targetList)

        for i in range(0,attr1Len,2):
            for j in range(0,attr2Len,2):
                if (i+1) < attr1Len and (j+1) < attr2Len:
                    anyList = list()
                    anyList.append(attackList[i])
                    anyList.append(cityList[j])
                    anyList.append(attackList[i+1])
                    anyList.append(cityList[j+1])
                    initialList.append(anyList)

        for i in range(0,attr1Len,2):
            for j in range(0,3,2):
                if (i+1) < attr1Len and (j+1) < 3:
                    anyList = list()
                    anyList.append(attackList[i])
                    anyList.append(targetList[j])
                    anyList.append(attackList[i+1])
                    anyList.append(targetList[j+1])
                    initialList.append(anyList)

        for i in range(0,attr2Len,2):
            for j in range(0,attr3Len,2):
                if (i+1) < attr2Len and (j+1) < attr3Len:
                    anyList = list()
                    anyList.append(cityList[i])
                    anyList.append(targetList[j])
                    anyList.append(cityList[i+1])
                    anyList.append(targetList[j+1])
                    initialList.append(anyList)

        if len(initialList)>16:
            del initialList[16:]
        return initialList


    def giveTopResultsListWithFrequency(self,cursor,tableName,initList,mainAttribute1,mainAttribute1Val,mainAttribute2,mainAttribute2Val):
        initListLen = len(initList)
        for i in range(0,initListLen):
            # query = "SELECT COUNT(*) as FREQUENCY FROM " + tableName " WHERE " + mainAttribute1 + " = " + "'" + mainAttribute1Val + "'" + " and " + mainAttribute2 + " = " + "'" + mainAttribute2Val + "' and "+ initList[i][0] +" = '" + initList[i][2] + "' and " + initList[i][1] + " = '" + initList[i][3] + "' "
            query = "SELECT COUNT(*) as FREQUENCY FROM " + tableName + " WHERE " + mainAttribute1 + " = " + "'" + mainAttribute1Val + "'" + " and " + mainAttribute2 + " = " + "'" + mainAttribute2Val + "'" + " and " + initList[i][0] + " = " + "'" + initList[i][2] + "'" + " and " + initList[i][1] + " = " + "'" + initList[i][3] + "'"
            try:
                cursor.execute(query)
                res = cursor.fetchall()
                for j in res:
                    a = j[0]
                    if a != "Unknown":
                        initList[i].append(a)
            except:
                print ("Unable to fetch data 1")
        return initList


    def generateTopResultsForThreeAttributes(self,cursor,handler,tableName,mainQueryCount,totalCount,mainAttribute1,mainAttribute1Val,mainAttribute2,mainAttribute2Val,attribute1,attribute2,attribute3):
        typeOneList = self.giveTopResultsList(cursor,tableName,attribute1,mainAttribute1,mainAttribute1Val,mainAttribute2,mainAttribute2Val)
        typeTwoList = self.giveTopResultsList(cursor,tableName,attribute2,mainAttribute1,mainAttribute1Val,mainAttribute2,mainAttribute2Val)
        typeThreeList = self.giveTopResultsList(cursor,tableName,attribute3,mainAttribute1,mainAttribute1Val,mainAttribute2,mainAttribute2Val)

        initialListWithoutFrequency = self.initialTwoFacetList(typeOneList,typeTwoList,typeThreeList)
        initialListWithFrequency = self.giveTopResultsListWithFrequency(cursor,tableName,initialListWithoutFrequency,mainAttribute1,mainAttribute1Val,mainAttribute2,mainAttribute2Val)
        twoFasetList = self.giveScoreSortedList(initialListWithFrequency,totalCount,mainQueryCount)
        # # printList(twoFasetList)
        # print "     2 Faset Recommendations     "
        # for i in twoFasetList:
        #     print i
        return twoFasetList
