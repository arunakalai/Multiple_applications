
from app1.views import surya
from app2.views import *
from django.urls import path

app_name='nothing'

urlpatterns=[
    path('surya/',surya,name='surya'),
]