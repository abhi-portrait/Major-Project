from random import randint
type = 1
number = 1
class recommendation:
    recArray = ['iyear','country_txt','city','attacktype1_txt','targtype1_txt','targsubtype1_txt','natlty1_txt','weaptype1_txt','dbsource']

    def moveOn(self,oneFasetList,twoFasetList,attr1,attr1Val,attr2,attr2Val):

        if type == 1:
            while 1>0:
                recParam1 = self.recArray[randint(0,8)]
                if recParam1 != oneFasetList[number-1][0]:
                    break
            while 1>0:
                recParam2 = self.recArray[randint(0,8)]
                if recParam2 != oneFasetList[number-1][0] and recParam2 != recParam1:
                    break
            while 1>0:
                recParam3 = self.recArray[randint(0,8)]
                if recParam3 != oneFasetList[number-1][0] and recParam3 != recParam1 and recParam3 != recParam2:
                    break

            attr1 = oneFasetList[number-1][0]
            attr1Val = oneFasetList[number-1][1]
            attr2 = ""
            attr2Val = ""
            return type,recParam1,recParam2,recParam3,attr1,attr1Val,attr2,attr2Val
        else:
            while 1>0:
                recParam1 = self.recArray[randint(0,8)]
                if recParam1 != twoFasetList[number-1][0]:
                    break
            while 1>0:
                recParam2 = self.recArray[randint(0,8)]
                if recParam2 != twoFasetList[number-1][0] and recParam2 != recParam1:
                    break
            while 1>0:
                recParam3 = self.recArray[randint(0,8)]
                if recParam3 != twoFasetList[number-1][0] and recParam3 != recParam1 and recParam3 != recParam2:
                    break
            attr1 = twoFasetList[number-1][0]
            attr1Val = twoFasetList[number-1][2]
            attr2 = twoFasetList[number-1][1]
            attr2Val = twoFasetList[number-1][3]
            return type,recParam1,recParam2,recParam3,attr1,attr1Val,attr2,attr2Val

        # else:
        #     while 1>0:
        #         recParam1 = self.recArray[randint(0,8)]
        #         if recParam1 != twoFasetList[number-1][0]:
        #             break
        #     while 1>0:
        #         recParam2 = self.recArray[randint(0,8)]
        #         if recParam2 != twoFasetList[number-1][0] and recParam2 != recParam1:
        #             break
        #     while 1>0:
        #         recParam3 = self.recArray[randint(0,8)]
        #         if recParam3 != twoFasetList[number-1][0] and recParam3 != recParam1 and recParam3 != recParam2:
        #             break
        #     attr1 = twoFasetList[number-1][0]
        #     attr1Val = twoFasetList[number-1][2]
        #     attr2 = twoFasetList[number-1][1]
        #     attr2Val = twoFasetList[number-1][3]
        #     return type,recParam1,recParam2,recParam3,attr1,attr1Val,attr2,attr2Val
