from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.login1, name="login"),
    path("register/", views.register, name="register")
]