from django.urls import path
from .views import *

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("form", views.form, name="form"),
    path("results", views.results, name="results"),
    path("results/<str:name>", views.results, name="custom_result")
]