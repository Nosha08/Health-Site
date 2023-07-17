from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import *
from .forms import *


def index(request):
    return render(request, 'index.html', {})


def form(request):
    if request.method == 'POST':
        form = OfficeForm1(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            opening_time = form.cleaned_data['open']
            closing_time = form.cleaned_data['close']
            location = form.cleaned_data['location']
            description = form.cleaned_data['description']
            office = form.save()
            return redirect('/medical/home', id=office.id) 
    else:
        form = OfficeForm1()

    return render(request, 'form.html', {'form': form})



def home(request):
    if request.method == 'POST':
        name1 = request.POST.get('query')
        print(name1)
        offices = Office.objects.all()
        for x in offices:
            if x.name == name1:
                print('Yes')
                print(x.id)
                return redirect('/medical/results/{id}'.format(id=x.id))
                
    return render(request, 'home.html', {})


def results(request, id):
    try:
       office = Office.objects.get(id=id)
    except Office.DoesNotExist:
        messages.error(request, 'Office not found.')
        return redirect('form')
    
    return render(request, 'results.html', {'office': office})