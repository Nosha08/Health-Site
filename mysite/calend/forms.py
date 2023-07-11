from django import forms
from django.forms import ModelForm
from .models import Appointment

class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ("__all__")