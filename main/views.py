from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index2(request,name):
    return HttpResponse(f'<h1>Hi {name}</h1>')
def index(request):
    return render(request,"index.html")
