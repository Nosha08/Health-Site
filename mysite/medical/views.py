from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import *
from .forms import *
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
time_choices = [900, 930, 1000, 1030, 1100, 1130, 1200, 
                1230, 1300, 1330, 1400, 1430, 1500, 1530, 
                1600, 1630, 1700, 1730, 1800, 1830, 1900, 1930,
                2000, 2030, 2100, 2130, 2200, 2230, 2300, 2330,
                2400, 2430]
time_choices1 = [1200, 1230, 100, 130, 200, 230, 300, 330,
                400, 430, 500, 530, 600, 630, 700, 730, 800,
                830, 900, 930, 1000, 1030, 1100, 1130, 1200, 
                1230, 100, 130, 200, 230, 300, 330, 400,
                430, 500, 530, 600, 630, 700, 730, 800, 830,
                900, 930, 1000, 1030, 1100, 1130]

@login_required(login_url='/user/login')
def index(request):
    return render(request, 'index.html', {})

def form(request):
    print("there")
    if request.method == 'POST':
        print("even more")
        form = OfficeForm1(request.POST)
        if form.is_valid():
            print("the most")
            name = form.cleaned_data['name']
            open = form.cleaned_data['open']
            close = form.cleaned_data['close']
            location = form.cleaned_data['location']
            description = form.cleaned_data['description']
            office = form.save()

            return redirect('/medical/results/{id}'.format(id=office.id), id=office.id) 
    else:
        form = OfficeForm1()

    return render(request, 'form.html', {'form': form})

@login_required(login_url='/user/login')
def home1(request):
    error = ''
    name1 = None
    if request.user.is_authenticated:
        username = request.user.username
    if request.method == 'POST':
        name1 = request.POST.get('query')
        print(name1)
        offices = Office.objects.all()
        office_names = []
        for i in offices:
            office_names.append(i)
        for x in offices:
            if x.name == name1:
                print('Yes')
                print(x.id)
                error = ''
                return redirect('/medical/results/{id}'.format(id=x.id))
            else:
                error = 'This office does not exist! Please try something else or create the page for it.'
                 
    offices = Office.objects.all()
    office_names = []
    for i in offices:
        office_names.append(i.name)    
    return render(request, 'home1.html', {'username': username, 'error': error, 'name1': name1})



def home(request):
    #error = ''
    #name1 = None
    """ if request.user.is_authenticated:
        username = request.user.username
    if request.method == 'POST':
        name1 = request.POST.get('query')
        print(name1)
        offices = Office.objects.all()
        office_names = []
        for i in offices:
            office_names.append(i)
        for x in offices:
            if x.name == name1:
                print('Yes')
                print(x.id)
                error = ''
                return redirect('/medical/results/{id}'.format(id=x.id))
            else:
                error = 'This office does not exist! Please try something else or create the page for it.'
                 """
    """ offices = Office.objects.all()
    office_names = []
    for i in offices:
        office_names.append(i.name)    """
    return render(request, 'home.html', {})

#print(time_options)
def results(request, id):

    try:
        office = Office.objects.get(id=id)
        new_open = str(office.open).split(':')
        new_open.pop(2)
        final_open = new_open[0] + new_open[1]
        new_close = str(office.close).split(':')
        new_close.pop(2)
        final_close = new_close[0] + new_close[1]

        available_times = []
        for x in time_choices:
            if int(final_open) <= x <= int(final_close):
                available_times.append(x)
        
        am_list = []
        pm_list = []

        available_times_new = []
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

        time_options = am_strings + pm_strings
    except Office.DoesNotExist:
        messages.error(request, 'Office not found.')
        return redirect('form')
    print(time_options)
    return render(request, 'results.html', {'form': form, 'office': office, 'time_options': time_options})

@login_required(login_url='/user/login')
def database(request):
    offices = Office.objects.all()
    return render(request, 'database.html', {'offices': offices})

@login_required(login_url='/user/login')
def about(request):
    return render(request, 'about.html', {})



def test(request):
    return render(request,'test.html',{})