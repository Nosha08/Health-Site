from django.db import models

# Create your models here.
class OfficeForm(models.Model):
    name = models.CharField(max_length=200)
    open = models.TimeField(auto_now=False, auto_now_add=False)
    close = models.TimeField(auto_now=False, auto_now_add=False)
    location = models.CharField(max_length=200)
