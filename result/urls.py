from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('result', views.result, name='result'),
    path('result_by_name', views.result_by_name, name='result_by_name')
]
