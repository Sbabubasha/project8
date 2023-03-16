from django.urls import path
from tolly.views import *




app_name='tolly'
urlpatterns=[
    path('prabhas/',prabhas,name='prabhas'),
    path('mahesh/',mahesh,name='mahesh'),
]