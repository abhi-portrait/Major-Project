import sys

sys.path.append('/home/abhi/Desktop/Django_Projects/mysite/polls/')
from django.http import HttpResponse
from . import main
from . import twoFasset
from SQLHandler import sqlHandler
from django.template import loader
from django.shortcuts import render
from . import process
import json

def index(request):
    # print(request.method)
    template = loader.get_template('polls/userQuery.html')
    return render(request, 'polls/userQuery.html')


def recommend(request):
    if request.method == 'POST':
        year = request.POST['year']
        country = request.POST['country']
    # else :
    #     return HttpResponse('invalid data')
        finalList = list()
        queryList = list()
        finalTwoFasetList = list()
        finalList = main.mainOneFaset("country_txt",country,"iyear",year)
        finalTwoFasetList = main.mainTwoFaset("country_txt",country,"iyear",year)
        queryList = sqlHandler.queryResultList
        # if finalList[0][0]=="U" or finalTwoFasetList[0][0]=="U":
        #     return HttpResponse('Data not available in database')
        return render(request, 'polls/recommendations.html', {'finalList':finalList,'queryList': queryList,'finalTwoFasetList':finalTwoFasetList})
    return HttpResponse('yo!')
    # return render(request, 'polls/recommendations.html')

# api for getting data
def second_recommend(request):
    if request.method == 'POST':
        id = request.POST['id']
        dataArr = request.POST['arr']
        data = json.loads(dataArr)
        print(type(data))
        # print(id)
        cid = id[:5]
        # print(cid)
        if cid == "trone":
            process.type = 1
            id = id[5:]
            process.number = int(id)
            main.mainRecommend(data[0],data[1],"","")
            fOList = main.finalOneFasetList
            fTList = main.finalTwoFasetList
            queryList = sqlHandler.queryResultList
        else:
            process.type = 2
            id = id[5:]
            process.number = int(id)
            main.mainRecommend(data[0],data[2],data[1],data[3])
            fOList = main.finalOneFasetList
            fTList = main.finalTwoFasetList
            queryList = sqlHandler.queryResultList
        # return render(request, 'polls/recommendations.html', {'finalList':fOList,'queryList': queryList,'finalTwoFasetList':fTList})
        retData = {'finalList':fOList,'queryList': queryList,'finalTwoFasetList':fTList}
        return HttpResponse(json.dumps(retData))
