from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def nazriya(request):
    return HttpResponse('<h2>nazriya is queen of the world</h2>')

def surya(request):
    return HttpResponse('<marquee>surya is my fav hero</marquee>')