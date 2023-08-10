from django.db import models
from django.urls import reverse

# Create your models here.
class OfficeForm(models.Model):
    name = models.CharField(max_length=200)
    open = models.TimeField(auto_now=False, auto_now_add=False)
    close = models.TimeField(auto_now=False, auto_now_add=False)
    location = models.CharField(max_length=200)
    description = models.CharField(max_length=400, default = "")



class Office(models.Model):
    name = models.CharField(max_length=200)
    open = models.TimeField(auto_now=False, auto_now_add=False)
    close = models.TimeField(auto_now=False, auto_now_add=False)
    location = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    def get_absolute_url(self):
        return reverse('results', args=[str(self.id)])
    
    def __str__(self):
        return self.name
    
class Rating(models.Model):
    office_rating = models.ForeignKey(Office, on_delete=models.CASCADE, related_name='ratings_received')
    stars = models.IntegerField()
