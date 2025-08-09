from django.shortcuts import render,redirect
from .models import Student,StudentHistory
# Create your views here.

def home(request):
    b=Student.objects.all()
    return render(request,'home.html',{'b':b})

def addtask(request):
    if request.method=='POST':
        a=request.POST['u']
        b=request.POST['t']
        c=request.POST['d']
        Student.objects.create(name=a,title=b,desc=c)
    return render(request,'schedule.html')

def history(request):
    c=StudentHistory.objects.all()
    return render(request,'history.html',{'c':c})

def update(request,id):
    t=Student.objects.get(id=id)
    if request.method=='POST':
        t.name=request.POST['a']
        t.title=request.POST['b']
        t.desc=request.POST['c']
        t.save()
        return redirect('home')
    return render(request,'update.html',{'t':t})

def delete(request,id):
    a=Student.objects.get(id=id)
    StudentHistory.objects.create(name=a.name, title=a.title, desc=a.desc)
    a.delete()
    return redirect('home')

def r_history(request):
    a=StudentHistory.objects.all()
    for i in a:
        Student.objects.create(name=i.name, title=i.title, desc=i.desc)
    a.delete()
    return redirect('history')

def d_history(request):
    a=StudentHistory.objects.all()
    a.delete()
    return redirect('history')
    
def r1_history(request, id):
    a=StudentHistory.objects.get(id=id)
    Student.objects.create(name=a.name, title=a.title, desc=a.desc)
    a.delete()
    return redirect('home')

def d1_history(request,id):
    a=StudentHistory.objects.get(id=id)
    a.delete()
    return redirect('history')