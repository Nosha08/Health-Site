from django.http import HttpResponse
from .forms import AppointmentForm
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world. You're at the calendar index!")

def create(request):
    render(request, 'templates/make_appointment.html',{})