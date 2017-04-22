import sys

# sys.path.append('/home/abhi/Desktop/Django_Projects/mysite/polls/')
from django.http import HttpResponse
from . import main
from django.template import loader
from django.shortcuts import render


def index(request):
    # print(request.method)
    # if request.method == 'POST':
    #     year = request.POST['year']
    #     country = request.POST['country']
    #     print(year)
    #     print(country)
    #     return HttpResponse('kldcblkndlkc')

    finalList = list()
    #  finalTwoList = list()
    finalList = main.main()
    # n = len(finalList)
    # m = len(finalList[0])
    #  finalTwoList = addOnToMain.listTwoFaset
    # template = loader.get_template('polls/userQuery.html')
    # return render(request, 'polls/userQuery.html')
    return render(request, 'polls/recommendations.html', {'finalList':finalList})
