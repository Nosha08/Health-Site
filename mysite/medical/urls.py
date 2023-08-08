from django.urls import path
from .views import *

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("form", views.form, name="form"),
    path("home", views.home, name="home"),
    path("home1", views.home1, name="home1"),
    path("welcome", views.home, name="welcome"),
    path("database", views.database, name="database"),
    path("about", views.about, name="about"),
    path("results/<int:id>", views.results, name="custom_result"),
    path("test", views.test, name="test"),
    path("submitted", views.submitted, name="submitted"),
]