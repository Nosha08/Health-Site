from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.login1, name="login"),
    path("logout/", views.logout1, name="logout"),
    path("register/", views.register, name="register"),
]