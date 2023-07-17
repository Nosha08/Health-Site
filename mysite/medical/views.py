from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import *


def index(request):
    return render(request, 'index.html', {})


def form(request):
    if request.method == 'POST':
        form = OfficeForm1(request.POST)
        if form.is_valid():
            global name, opening_time, closing_time, location, description
            name = form.cleaned_data['name']
            opening_time = form.cleaned_data['open']
            closing_time = form.cleaned_data['close']
            location = form.cleaned_data['location']
            description = form.cleaned_data['description']
            form.save()
            return redirect('/medical/results') 
    else:
        form = OfficeForm1()

    return render(request, 'form.html', {'form': form})


def results(request):
   return render(request, 'results.html', {'name': name, 'opening_time': opening_time, 'closing_time': closing_time, 'location': location, 'description': description})