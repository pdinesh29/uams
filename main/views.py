from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request,"index.html")
def student(request,name):
    if name in ['A22126511167','A22126511134','A22126511135']:
        return HttpResponse('<h1>creator</h1><h1 style="color: green; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); font-size: 300px;">91%</h1>')
    return HttpResponse('<h1 style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); font-size: 100px;">75%</h1>')
def edit(request):
    return render(request,"edit.html")