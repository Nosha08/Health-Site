from django.db import models

# Create your models here.

class Appointment(models.Model):
    time = models.IntegerField()
    date = models.DateField()
    def __str__(self):
        return "Date: " + self.date + " Time: " + self.time + ":00"