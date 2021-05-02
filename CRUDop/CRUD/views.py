from django.shortcuts import render
from django.contrib import messages
from .models import billmodel
from .forms import cusforms
from django.http import Http404


def showcustomer(request):
    showall = billmodel.objects.all()
    return render(request, 'index.html', {"data": showall})


def insertcustomer(request):
    if request.method == "POST":
        if request.POST.get('donor_id') and request.POST.get('donor_name') and request.POST.get('email') and request.POST.get('blood_group') and request.POST.get('gender') and request.POST.get('donated_amount') and request.POST.get('prev_donated'):
            saverecord = billmodel()
            saverecord.donor_id = request.POST.get('donor_id')
            saverecord.donor_name = request.POST.get('donor_name')
            saverecord.email = request.POST.get('email')
            saverecord.blood_group = request.POST.get('blood_group')
            saverecord.gender = request.POST.get('gender')
            saverecord.donated_amount = request.POST.get('donated_amount')
            saverecord.prev_donated = request.POST.get('prev_donated')
            saverecord.save()
            messages.success(request, 'Donor ' +
                             saverecord.donor_name+' is saved sucessfully')
            return render(request, 'insert.html')

    else:
        return render(request, 'insert.html')

def editcus(request, donor_id):
    editcusobj = billmodel.objects.get(donor_id=donor_id)
    return render(request, 'edit.html', {"billmodel": editcusobj})


def updatecus(request,donor_id):
    Updatecus = billmodel.objects.get(donor_id=donor_id)
    form = cusforms(request.POST, instance=Updatecus)
    if form.is_valid():
        form.save()
        messages.success(request, 'Record Updated')
        return render(request, 'edit.html', {"billmodel": Updatecus})
    else:
        editcus(request, donor_id)

def delcus(request, donor_id):
    delcus = billmodel.objects.get(donor_id=donor_id)
    delcus.delete()
    showdata = billmodel.objects.all()
    print(showdata)
    return render(request, 'index.html', {"data": showdata})
