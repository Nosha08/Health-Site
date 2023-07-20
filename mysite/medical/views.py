from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import *
from .forms import *
from datetime import datetime

time_choices = [900, 930, 1000, 1030, 1100, 1130, 1200, 
                1230, 1300, 1330, 1400, 1430, 1500, 1530, 
                1600, 1630, 1700, 1730, 1800, 1830, 1900, 1930]
time_choices1 = [900, 930, 1000, 1030, 1100, 1130, 1200, 
                 1230, 100, 130, 200, 230, 300, 330, 400,
                 430, 500, 530, 600, 630]

def index(request):
    return render(request, 'index.html', {})


def form(request):
    if request.method == 'POST':
        form = OfficeForm1(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            open = form.cleaned_data['open']
            close = form.cleaned_data['close']
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


available_times_new = []
am_list = []
pm_list = []
""" am_strings = [f"{str(time)[:-2]}:{str(time)[-2:]} AM" for time in am_list]
pm_strings = [f"{str(time)[:-2]}:{str(time)[-2:]} PM" for time in pm_list]
time_options = am_strings + pm_strings """

#print(time_options)
def results(request, id):
    try:
        office = Office.objects.get(id=id)
        new_open = str(office.open).split(':')
        new_open.pop(2)
        final_open = new_open[0] + new_open[1]
        print(final_open)
        new_close = str(office.close).split(':')
        new_close.pop(2)
        final_close = new_close[0] + new_close[1]
        print(final_close)

        available_times = []
        for x in time_choices:
            print(x)
            if int(final_open) <= x <= int(final_close):
                available_times.append(x)
        
        
        for x in available_times:
            if x > 1259:
                available_times_new.append(x - 1200)
                pm_list.append(x - 1200)
            else:
                available_times_new.append(x)
                am_list.append(x)


        am_strings = [f"{str(time)[:-2]}:{str(time)[-2:]} AM" for time in am_list]
        pm_strings = [f"{str(time)[:-2]}:{str(time)[-2:]} PM" for time in pm_list]
        time_options = am_strings + pm_strings
        print(time_options)
        #time_options.clear()
          
    except Office.DoesNotExist:
        messages.error(request, 'Office not found.')
        return redirect('form')
    print(time_options)
    return render(request, 'results.html', {'office': office, 'time_options': time_options})

def database(request):
    offices = Office.objects.all()
    return render(request, 'database.html', {'offices': offices})
