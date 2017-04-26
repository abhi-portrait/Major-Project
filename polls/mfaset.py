import MySQLdb
import operator
from operator import itemgetter


mainAttribute1 = "country_txt"
mainAttribute2 = "iyear"
attribute1 = "attacktype1_txt"
attribute2 = "city"
attribute3 = "targtype1_txt"
twoFasetList = list()

# def printList(someList):
#     for i in range(0,9):
#         print "[ '%s' : '%s' , '%s' : '%s' , '%s']" %(someList[i][0],someList[i][2],someList[i][1],someList[i][3],someList[i][5])



def getCount(query):
    db = MySQLdb.connect("127.0.0.1","root","","Terrorism")
    cursor = db.cursor()
    c = 0
    try:
        cursor.execute(query)
        res = cursor.fetchall()
        c = res[0][0]
    except:
        print ("Unable to fetch data")

    return c

def makeQuery(attribute1,attributeVal1,attribute2,attributeVal2):
    s = "SELECT COUNT(*) FROM attacks where " + attribute1 + " = '" + attributeVal1 + "' and " + attribute2 + " = '" + attributeVal2 + "' "
    return s

def giveScoreSortedList(someList,totalCount,mainQueryCount):

    if totalCount == 0 or mainQueryCount == 0:
        sortedTwoFacetList = list()
        sortedTwoFacetList.append("Unable to fetch data")
        return sortedTwoFacetList
    someListLen = len(someList)
    for i in range(0,someListLen):
        num = someList[i][4] / (6 * 1.0)
        denomNum = getCount(makeQuery(someList[i][0],someList[i][2],someList[i][1],someList[i][3]))
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


def giveTopResultsList(attribute,year,country):
    db = MySQLdb.connect("127.0.0.1","root","","Terrorism")
    cursor = db.cursor()

    query  = "SELECT " + attribute + ", count(*) as Frequency FROM attacks where " + mainAttribute1 + " = " + "'" + country + "'" + " and " + mainAttribute2 + " = " + "'" + year + "'" + " GROUP BY " + attribute + " ORDER BY COUNT(*) DESC LIMIT 5"
    listType = list()
    try:
        cursor.execute(query)
        res = cursor.fetchall()
        for i in res:
            a = attribute
            b = i[0]
            listType.append(a)
            listType.append(b)
    except:
        print ("Unable to fetch data")

    return listType

def  initialTwoFacetList(attackList,cityList,targetList):


    initialList = list()
    # if len(attackList)<3 or len(cityList)<3 or len(targetList)<3 :
    #     initialList.append("Unable to fetch data")
    #     return initialList
    attr1Len = len(attackList)
    attr2Len = len(cityList)
    attr3Len = len(targetList)

    for i in range(0,attr1Len,2):
        for j in range(0,attr2Len,2):
            anyList = list()
            anyList.append(attackList[i])
            anyList.append(cityList[j])
            anyList.append(attackList[i+1])
            anyList.append(cityList[j+1])
            initialList.append(anyList)

    for i in range(0,attr1Len,2):
        for j in range(0,3,2):
            anyList = list()
            anyList.append(attackList[i])
            anyList.append(targetList[j])
            anyList.append(attackList[i+1])
            anyList.append(targetList[j+1])
            initialList.append(anyList)

    for i in range(0,attr2Len,2):
        for j in range(0,attr3Len,2):
            anyList = list()
            anyList.append(cityList[i])
            anyList.append(targetList[j])
            anyList.append(cityList[i+1])
            anyList.append(targetList[j+1])
            initialList.append(anyList)

    if len(initialList)>16:
        del initialList[16:]
    return initialList

def giveTopResultsListWithFrequency(initList,year,country):
    db = MySQLdb.connect("127.0.0.1","root","","Terrorism")
    cursor = db.cursor()
    initListLen = len(initList)
    for i in range(0,initListLen):
        query  = "SELECT  count(*) as Frequency FROM attacks where " + mainAttribute1 + " ='" + country + "'  and " + mainAttribute2 + " ='" + year + "' and "+ initList[i][0] +" = '" + initList[i][2] + "' and " + initList[i][1] + " = '" + initList[i][3] + "' "

        try:
            cursor.execute(query)
            res = cursor.fetchall()
            for j in res:
                a = j[0]
                initList[i].append(a)
        except:
            print ("Unable to fetch data")

    return initList

def generateTopResultsForRestAttributes(mainQueryCount,totalCount,year,country):

    attackList = giveTopResultsList(attribute1,year,country)
    cityList = giveTopResultsList(attribute2,year,country)
    targetList = giveTopResultsList(attribute3,year,country)

    initialListWithoutFrequency = initialTwoFacetList(attackList,cityList,targetList)
    if initialListWithoutFrequency[0]=="Unable to fetch data":
        return initialListWithoutFrequency
    initialListWithFrequency = giveTopResultsListWithFrequency(initialListWithoutFrequency,year,country)
    twoFasetList = giveScoreSortedList(initialListWithFrequency,totalCount,mainQueryCount)
    return twoFasetList
    # printList(twoFasetList)
    # print "     2 Faset Recommendations     "
    # for i in twoFasetList:
    #     print i


def takeUserInputs(year,country):
    query = "SELECT count(*) from attacks where " + mainAttribute1 + " ='" + country + "'  and " + mainAttribute2 + " ='" + year + "' "
    mainQueryCount = getCount(query)
    totalCount = getCount("SELECT count(*) from attacks")
    return generateTopResultsForRestAttributes(mainQueryCount,totalCount,year,country)

# def main():
#     takeUserInputs()


# if __name__ == '__main__':
#     main()
