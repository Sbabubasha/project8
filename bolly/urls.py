from django.urls import path
from bolly.views import *



app_name ='bolly'


urlpatterns =[
    path('salman/',salman,name='salman'),
    path('tiger/',tiger,name='tiger'),
]
