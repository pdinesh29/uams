from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import *
def login(request):
    if 'id' in request.session:
        return redirect(reverse("home"))
    else:
        return render(request,"index.html")
def student(request,name):
    if name in ['A22126511167','A22126511134','A22126511135']:
        return HttpResponse('<h1>creator</h1><h1 style="color: green; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); font-size: 300px;">91%</h1>')
    return HttpResponse('<h1 style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); font-size: 100px;">75%</h1>')
def home(request):
    if request.method=='GET':
        if "id" not in request.session:
            request.session["wrongp"]=False
            return  redirect('login')
        else:
            print(request.session['id'])
            faculty=Faculty.objects.get(id=request.session['id'])
            return render(request, "home.html", {
                    "nums": Alloted.objects.filter(faculty=faculty),
                })
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('pass')
        try:
            faculty = Faculty.objects.get(email=email,password=password)
            request.session['id']=faculty.id
            return render(request, "home.html", {
                    "nums": Alloted.objects.filter(faculty=faculty),
                })
        except Faculty.DoesNotExist:
            request.session['wrongp']=True
            return redirect('login')
    return redirect('login')
def logout(request):
    request.session.flush()
    return redirect('home')
# def modifyy(request):
#     return render(request,'modifyy.html')
# def createe(request):
#     return render(request,'createe.html')