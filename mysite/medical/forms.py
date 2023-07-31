from django import forms
from django.forms import ModelForm
from .models import *

class OfficeForm1(ModelForm):
    class Meta:
        model = Office
        fields = ('__all__')
        widgets = {
            'open': forms.TimeInput(attrs={'type': 'time'}),
            'close': forms.TimeInput(attrs={'type': 'time'}),
        }
        input_formats = {
            'open': ['%H:%M'],
            'close': ['%H:%M'],
        }