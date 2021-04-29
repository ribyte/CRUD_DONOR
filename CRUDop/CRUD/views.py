from django.shortcuts import render
from django.contrib import messages
from .models import billmodel

def showcustomer(request):
    showall=billmodel.objects.all()
    return render(request,'index.html',{"data":showall})

def insertcustomer(request):
    if request.method=="POST":
        if request.POST.get('c_id') and request.POST.get('c_name') and request.POST.get('email') and request.POST.get('gender') and request.POST.get('watt_used'):
            saverecord=billmodel()
            saverecord.c_id=request.POST.get('c_id')
            saverecord.c_name=request.POST.get('c_name')
            saverecord.email=request.POST.get('email')
            saverecord.gender=request.POST.get('gender')
            saverecord.watt_used=request.POST.get('watt_used')
            saverecord.save()
            messages.success(request,'Customer '+saverecord.c_name+' is saved sucessfully')
            return render(request,'insert.html')
    
    else:
        return render(request,'insert.html')