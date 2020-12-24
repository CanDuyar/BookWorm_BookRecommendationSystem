
from django import urls
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('user_choice', views.user_choice, name='user_choice'),
    path('result1', views.result1, name='result1'),
    path('result2', views.result2, name='result2'),
    path('search_result', views.search_result, name='search_result')
]