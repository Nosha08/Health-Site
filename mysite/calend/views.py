from django.http import HttpResponse, HttpResponseRedirect
from .forms import AppointmentForm
from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Appointment
from datetime import date
def index(request):
    return HttpResponse("Hello, world. You're at the calendar index!")

# def calendar(request,year,month,day = '1'):

def create(request, year=2023, month="January", day = 1):
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
    for i in months:
        if i == month:
            month_number = months[i]
    cal = HTMLCalendar().formatmonth(year,month_number)

    now = datetime.now()
    current_year = now.year


    appointment_list = Appointment.objects.all()
    send_date = date(int(year), int(month_number), int(day))

    submitted = False
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            print("cdc")
            form.save()
            
            return HttpResponseRedirect('/calendar/make_appointment?submitted=True')
    else:
        form = AppointmentForm
        if "submitted" in request.GET:
            submitted = True
    appointments_all = Appointment.objects.all().filter(date = send_date)
    times = []
    for objects in appointments_all:
        times.append(objects.time)        
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
        "times":times,
        })