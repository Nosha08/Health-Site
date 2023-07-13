from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *


def index(request):
    return render(request, 'index.html', {})


def form(request):
    if request.method == 'GET':
        form = OfficeForm
        print(form)
        return render(request, 'form.html', {'form', form})

    '''
    if request.method == 'POST':
        form = OfficeForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'form.html', {'form', form})
    else:
        
        if "submitted" in request.GET:
            submitted = True
        if name and open and close and location != '':
            return redirect('/medical/results')
        else:
            return redirect('/medical/form')'''
    
    return render(request, 'form.html', {'form', form})

def results(request):
    pass
   # return render(request, 'results.html', {'name': name, 'open': open, 'close': close, 'location': location})