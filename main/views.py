from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
def index(request):
    return render(request,"index.html",{
        "wrong": False
    })
def student(request,name):
    if name in ['A22126511167','A22126511134','A22126511135']:
        return HttpResponse('<h1>creator</h1><h1 style="color: green; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); font-size: 300px;">91%</h1>')
    return HttpResponse('<h1 style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); font-size: 100px;">75%</h1>')
def edit(request):
    if request.method=="GET":
        if "id" not in request.session:
            return  redirect('index')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('pass')

        try:
            faculty = Faculty.objects.get(email=email,password=password)
            return render(request, "edit.html", {
                    "nums": Alloted.objects.filter(faculty=faculty),
                })
        except Faculty.DoesNotExist:
            return render(request, "index.html", {
                "wrong": True
            })
    
    return render(request, "index.html")