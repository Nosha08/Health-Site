from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("make_appointment/", views.create, name = "create"),
    path("calender/<int:id>/", views.create, name = "create"),
    path("calender/<int:id>/<int:year>/", views.create, name = "create"),
    path("calender/<int:id>/<int:year>/<str:month>/", views.create, name = "create"),
    path("calender/<int:id>/<int:year>/<str:month>/<int:day>/", views.create, name = "create")
]