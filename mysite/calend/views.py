from django.http import HttpResponse, HttpResponseRedirect
from .forms import AppointmentForm
from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime

def index(request):
    return HttpResponse("Hello, world. You're at the calendar index!")

def calendar(request,year,month):
    month = month.capitalize()
    months = {
        "January":1,
        "February":2,
        "March":3,
        "April":4,
        "May":5,
        "June":6,
        "July":7,
        "August":8,
        "September":9,
        "October":10,
        "November":11,
        "December":12
    }
    for i in months:
        if i == month:
            month_number = months[i]
    cal = HTMLCalendar().formatmonth(year,month_number)

    now = datetime.now()
    current_year = now.year
    return render(request, 'calender.html',{
        "year":year,
        "month":month,
        "month_number": month_number,
        "cal": cal,
        "current_year": current_year,
        })

def create(request):
    submitted = False
    print("sddscdsdc")
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        print(form)
        if form.is_valid():
    
            form.save()
            
            return HttpResponseRedirect('/calendar/make_appointment?submitted=True')
    else:
        form = AppointmentForm
        if "submitted" in request.GET:
            submitted = True
    return render(request, 'make_appointment.html',{'form': form, "submitted": submitted})
