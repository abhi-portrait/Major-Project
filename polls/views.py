import sys

sys.path.append('/home/abhi/Desktop/Django_Projects/mysite/polls/')
from django.http import HttpResponse
from . import main
from . import mfaset
from SQLHandler import sqlHandler
from django.template import loader
from django.shortcuts import render


def index(request):
    # print(request.method)

    #     print(year)
    #     print(country)
    #     return HttpResponse('kldcblkndlkc')
    template = loader.get_template('polls/userQuery.html')
    return render(request, 'polls/userQuery.html')



def recommend(request):
    if request.method == 'POST':
        year = request.POST['year']
        country = request.POST['country']
    finalList = list()
    queryList = list()
    finalTwoFasetList = list()

    #  finalTwoList = list()
    # main.takeUserInputs(year,country)
    finalList = main.main(year,country)
    finalTwoFasetList = mfaset.takeUserInputs(year,country)
    queryList = sqlHandler.queryResultList
    # n = len(finalList)
    # m = len(finalList[0])
    #  finalTwoList = addOnToMain.listTwoFaset

    return render(request, 'polls/recommendations.html', {'finalList':finalList,'queryList': queryList,'finalTwoFasetList':finalTwoFasetList})
