from django.shortcuts import render
from .models import billModel

def showcustomer(request):
    showall=billModel.objects.all()
    return render(request,'index.html',{"data":showall})