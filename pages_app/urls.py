
from django import urls
from . import views
from django.urls import path

urlpatterns = [
    path('', views.login, name='login'),
    path('home', views.home, name='home'),
    path('user_choise', views.user_choise, name='user_choise'),
    path('result', views.result, name='result')
]
