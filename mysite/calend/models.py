from django.db import models

# Create your models here.
TIME_CHOICES = (
    ('9:00', '9:00 AM'),
    ('9:30', '9:30 AM'),
    ('10:00', '10:00 AM'),
    ('10:30', '10:30 AM'),
    ('11:00', '11:00 AM'),
    ('11:30', '11:30 AM'),
    ('12:00', '12:00 AM'),
    ('12:30', '12:30 AM'),
    ('13:00', '1:00 PM'),
    ('13:30', '1:30 PM'),
    ('14:00', '2:00 PM'),
    ('14:30', '2:30 PM'),
    ('15:00', '3:00 PM'),
    ('15:30', '3:30 PM'),
    ('16:00', '4:00 PM'),
    ('16:30', '4:30 PM'),
    ('17:00', '5:00 PM'),
    ('17:30', '5:30 PM'),
    ('18:00', '6:00 PM'),
    ('18:30', '6:30 PM'),
)
class Appointment(models.Model):
    date = models.DateField()
    time = models.CharField(max_length = 20, choices = TIME_CHOICES)

    def __str__(self):
        return "Date: " + str(self.date) + " Time: " + str(self.time) + ":00"