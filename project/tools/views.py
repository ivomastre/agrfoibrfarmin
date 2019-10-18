from django.http import HttpResponse
from django.shortcuts import render
from . import connect_db
from . import algTempo
from . import algAcao
from django.views.decorators.csrf import csrf_exempt
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from . import a
import json
# Create your views here.

def tables(request):
    #em construção
    x = a.create_connection("D:\\sqlite\db\pythonsqlite.db")
    cidadeList = connect_db.select_all_tempo(x)
    y = []
    for x in cidadeList:
        y.append(cidadeUsavel(x[1], x[2], x[3], x[4], x[5]))
    cidadeList = y
    return render(request, 'tools/tables.html', {'cidadeList': cidadeList })

@csrf_exempt
def get_acao(request):
    alo =""
    if request.method == 'GET':
        form = request.GET.get('nome')
        alo = algAcao.PegarAcao(form)
    return HttpResponse(alo , content_type="application/json")
def get_cidade(request):
    if request.method == 'GET':
        form = request.GET.get('cidadeNome')
           # return HttpResponse(HolyMoly(cidade), content_type="application/json")
        yareyare = algTempo.HolyMoly(form)
        return HttpResponse(yareyare , content_type="application/json")
class cidadeUsavel:
    def __init__(self, cidade, tempMin, tempMax, umidadeMin, umidadeMax):
        self.cidade = cidade
        self.tempMin = tempMin
        self.tempMax = tempMax
        self.tempMin = tempMin
        self.umidadeMax = umidadeMax
        self.umidadeMin = umidadeMin