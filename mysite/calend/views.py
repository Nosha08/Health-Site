from django.http import HttpResponse, HttpResponseRedirect
from .forms import AppointmentForm
from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import *
from datetime import date
from medical.views import *

def index(request):
    return HttpResponse("Hello, world. You're at the calendar index!")

# def calendar(request,year,month,day = '1'):
current_year = datetime.now().year
current_day = datetime.now().day
today = datetime.now()

current_month = today.strftime("%B")

print(current_month)
def create(request,office_id= 1, year=int(current_year), month=str(current_month), day = 1):
    month = month.capitalize()
    form = AppointmentForm

    TIME_CHOICES = {
        '9:00': '9:00 AM',
        '9:30': '9:30 AM',
        '10:00': '10:00 AM',
        '10:30': '10:30 AM',
        '11:00': '11:00 AM',
        '11:30': '11:30 AM',
        '12:00': '12:00 AM',
        '12:30': '12:30 AM',
        '13:00': '1:00 PM',
        '13:30': '1:30 PM',
        '14:00': '2:00 PM',
        '14:30': '2:30 PM',
        '15:00': '3:00 PM',
        '15:30': '3:30 PM',
        '16:00': '4:00 PM',
        '16:30': '4:30 PM',
        '17:00': '5:00 PM',
        '17:30': '5:30 PM',
        '18:00': '6:00 PM',
        '18:30': '6:30 PM'
    }
    TIME_LIST = TIME_CHOICES.values()
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

    available_times_new = []
    am_list = []
    pm_list = []

    office = Office.objects.get(id=office_id)
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


    for i in months:
        if i == month:
            month_number = months[i]
    cal = HTMLCalendar().formatmonth(year,month_number)

    now = datetime.now()
    current_year = now.year
    appointment_list = Appointment.objects.all()
    send_date = date(int(year), int(month_number), int(day))

    submitted = False
    duplicate = False
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            for i in appointment_list:
                if i.time == form.cleaned_data["time"] and i.date == form.cleaned_data["date"] and i.office_id == form.cleaned_data["office_id"]:
                    return HttpResponseRedirect('/calendar/make_appointment?duplicate=True')
            form.save()
            
            return HttpResponseRedirect(f'/calendar/make_appointment/{office_id}/?submitted=True')
    else:
        form = AppointmentForm
        if "submitted" in request.GET:
            submitted = True
        if "duplicate" in request.GET:
            duplicate = True
    appointments_all = Appointment.objects.all().filter(date = send_date, office_id = office_id)
    appointments_month = Appointment.objects.all().filter(month = month_number, year = year, office_id = office_id)

    times = []
    times_len = len(time_options)
    for objects in appointments_all:
        times.append(objects.time)

    filled = []
    for i in range(32):
        filled.append(0)

    for j in appointments_month:
        for i in range(32):
            if j.day == i:
                filled[i] += 1
    return render(request, 'calender.html',{
        "year":year,
        "month":month,
        "day":day,
        "month_number": month_number,
        "cal": cal,
        "current_year": current_year,
        "appointment_list": appointment_list,
        "date": send_date,
        "form": form,
        "submitted": submitted,
        "time_choices": TIME_CHOICES,
        "time_list": TIME_LIST,
        "appointments_all": appointments_all,
        "times": times,
        "times_len": times_len,
        "filled": filled,
        "duplicate": duplicate,
        "office_id":office_id,
        "time_options":time_options,
        })