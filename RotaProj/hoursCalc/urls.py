from django.contrib import admin
from django.urls import path
from . import views as shift_views
from django.contrib.auth import views as auth_views

# app_name = 'rota'

urlpatterns = [
    path('', shift_views.index, name="index"),
    path('first/', shift_views.initial_page, name="initial_page"),
    path('submit/', shift_views.submitForm, name='submit'),
    path('select/', shift_views.selectDate, name='select'),
    path('edit/<int:pk>/', shift_views.update_shift, name='edit'),
    path('detail/<int:pk>/', shift_views.shift_detail, name='detail'),
    path('remove/<int:pk>/', shift_views.remove, name='remove'),
    path('select/<str:date_from>/<str:date_to>/', shift_views.select_periods, name='select'),


    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]