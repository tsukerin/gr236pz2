from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index),
    re_path(r'^catalog/(?P<product>\d+)/(?P<name_product>\D+)', categories),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
    re_path('catalog/', categories)
]