from django.urls import path
from .views import *

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("form", views.form, name="form"),
    path("home", views.home, name="home"),
    path("database", views.database, name="database"),
    path("results/<int:id>", views.results, name="custom_result")
]