from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('result_by_name', views.result_by_name, name='result_by_name'),
    path('result', views.result, name='result'),
    path('student', views.student, name='student')
]