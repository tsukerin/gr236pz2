from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


# Create your views here.
def index(request):
   return render(request, 'index.html')

def categories(request, product = 0, name_product = "НЕ НАЙДЕНО"):
   product_type = request.GET.get('type', 'Не задан тип продукта')
   output = f'<h1>Продукт №{product}:{name_product}. Тип продукта: {product_type}</h1>'
   return HttpResponse(output)

def archive(request, year):
   return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')

def pageNotFound(request, exception):
   return HttpResponseNotFound('<center><h5>Страница не найдена</h5></center>')