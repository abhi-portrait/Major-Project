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

    for i in range(0,9):
        num = someList[i][4] / (mainQueryCount * 1.0)
        denomNum = getCount(makeQuery(someList[i][0],someList[i][2],someList[i][1],someList[i][3]))
        denom = denomNum / (totalCount * 1.0)
        if denom != 0:
            score = num / (denom * 1.0)
            someList[i].append(score)
    tempList = list()
    for i in range(0,9):
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
    anyList = list()
    initialList = list()

    anyList.append(attackList[0])
    anyList.append(cityList[0])
    anyList.append(attackList[1])
    anyList.append(cityList[1])
    initialList.append(anyList)

    bList = list()
    bList.append(cityList[0])
    bList.append(targetList[0])
    bList.append(cityList[1])
    bList.append(targetList[1])
    initialList.append(bList)

    cList = list()
    cList.append(attackList[0])
    cList.append(targetList[0])
    cList.append(attackList[1])
    cList.append(targetList[1])
    initialList.append(cList)

    dList = list()
    dList.append(attackList[0])
    dList.append(cityList[2])
    dList.append(attackList[1])
    dList.append(cityList[3])
    initialList.append(dList)

    eList = list()
    eList.append(attackList[0])
    eList.append(targetList[2])
    eList.append(attackList[1])
    eList.append(targetList[3])
    initialList.append(eList)

    fList = list()
    fList.append(cityList[0])
    fList.append(targetList[2])
    fList.append(cityList[1])
    fList.append(targetList[3])
    initialList.append(fList)

    gList = list()
    gList.append(cityList[0])
    gList.append(attackList[2])
    gList.append(cityList[1])
    gList.append(attackList[3])
    initialList.append(gList)

    hList = list()
    hList.append(targetList[0])
    hList.append(attackList[2])
    hList.append(targetList[1])
    hList.append(attackList[3])
    initialList.append(hList)

    iList = list()
    iList.append(targetList[0])
    iList.append(cityList[2])
    iList.append(targetList[1])
    iList.append(cityList[3])
    initialList.append(iList)

    return initialList

def giveTopResultsListWithFrequency(initList,year,country):
    db = MySQLdb.connect("127.0.0.1","root","","Terrorism")
    cursor = db.cursor()

    for i in range(0,9):
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

    initialListWithFrequency = giveTopResultsListWithFrequency(initialListWithoutFrequency,year,country)
    twoFasetList = giveScoreSortedList(initialListWithFrequency,totalCount,mainQueryCount)
    return twoFasetList
    # printList(twoFasetList)
    # print "     2 Faset Recommendations     "
    # for i in twoFasetList:
    #     print i


def takeUserInputs(year,country):
    query = "SELECT count(*) from attacks where iyear = " + "'" + year + "'" + " and country_txt = " + "'" + country + "'"
    mainQueryCount = getCount(query)
    totalCount = getCount("SELECT count(*) from attacks")
    return generateTopResultsForRestAttributes(mainQueryCount,totalCount,year,country)

# def main():
#     takeUserInputs()


# if __name__ == '__main__':
#     main()
