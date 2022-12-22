from django.urls import path
from . import views

#write your views here
urlpatterns=[
    path('', views.index, name='index'),
    path('about/', views.About, name='about')
]