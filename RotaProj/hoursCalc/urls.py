from django.contrib import admin
from django.urls import path
from . import views

# app_name = 'rota'

urlpatterns = [
    path('', views.index, name="index"),
    path('submit/', views.submitForm, name='submit'),
    path('select/', views.selectDate, name='select'),
    path('select/', views.selectDate, name='select'),
    path('remove/<int:pk>/', views.remove, name='remove'),
    path('select/<str:date_from>/<str:date_to>/', views.select_periods, name='select'),
]