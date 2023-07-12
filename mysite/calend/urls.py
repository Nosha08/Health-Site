from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("make_appointment/", views.create, name = "create"),
    path("calender/<int:year>/<str:month>/", views.calendar, name = "calender")
]