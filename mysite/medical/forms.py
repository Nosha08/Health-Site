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

class RatingForm(forms.Form):
    stars = forms.ChoiceField(choices=[(5, '5'), (4, '4'), (3, '3'), (2, '2'), (1, '1')])