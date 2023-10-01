from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


# Create your views here.
def index(request):
   return HttpResponse('<center><h2>Hello</h2></center>')

def categories(request, id):
   print(request.GET)
   return HttpResponse(f'<h1>Категория: </1><p>{id}</p>')

def archive(request, year):
   return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')

def pageNotFound(request, exception):
   return HttpResponseNotFound('<center><h5>Страница не найдена</h5></center>')