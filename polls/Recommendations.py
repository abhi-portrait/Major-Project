import MySQLdb
import two_facet
import addOnToMain
from random import randint

print "Select the type of recommendations"
type = raw_input()
print "Select the order no. of recommendation"
number = raw_input()

recArray = ['iyear','country_txt','city','attacktype1_txt','targtype1_txt','targsubtype1_txt','natlty1_txt','weaptype1_txt','dbsource']

if type == 1:
    while 1>0:
        recParam1 = recArray[randint(0,8)]
        if recParam1 != faSetList[number-1][0]:
            break
    while 1>0:
        recParam2 = recArray[randint(0,8)]
        if recParam2 != faSetList[number-1][0]:
            break
    while 1>0:
        recParam3 = recArray[randint(0,8)]
        if recParam3 != faSetList[number-1][0]:
            break
    #use function as named in files
    fun(faSetList[number-1][0],faSetList[number-1][1],recParam1,recParam2,recParam3)

else:
    while 1>0:
        recParam1 = recArray[randint(0,8)]
        if recParam1 != twoFasetList[number-1][0] and recParam1 != twoFasetList[number-1][2]:
            break
    while 1>0:
        recParam2 = recArray[randint(0,8)]
        if recParam2 != twoFasetList[number-1][0] and recParam2 != twoFasetList[number-1][2]:
            break
    while 1>0:
        recParam3 = recArray[randint(0,8)]
        if recParam3 != twoFasetList[number-1][0] and recParam3 != twoFasetList[number-1][2]:
            break
    #use function as named in files
    fun(twoFasetList[number-1][0],twoFasetList[number-1][1],twoFasetList[number-1][2],twoFasetList[number-1][3],recParam1,recParam2,recParam3)
