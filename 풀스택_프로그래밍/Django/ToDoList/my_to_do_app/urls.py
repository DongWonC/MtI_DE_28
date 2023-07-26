# -*- coding:utf-8 -*-

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index) # views.py 파일에서 index 함수를 찾아!
]