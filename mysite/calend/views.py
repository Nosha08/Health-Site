from django.http import HttpResponse, HttpResponseRedirect
from .forms import AppointmentForm
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world. You're at the calendar index!")

def appointment(request):
    return render(request, 'make_appointment.html',{})

def create(request):
    submitted = False
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect('/calendar/make_appointment?submitted=True')
    else:
        form = AppointmentForm
        if "submitted" in request.GET:
            submitted = True
    return render(request, 'make_appointment.html',{'form': form, "submitted": submitted})
