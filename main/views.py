from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index2(request):
    return HttpResponse('index.html')
def index(request):
    return render(request,"index.html")
