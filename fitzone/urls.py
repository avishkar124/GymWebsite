from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("programs/", views.programs, name="programs"),
    path("trainers/", views.trainers, name="trainers"),
    path("contact/", views.contact, name="contact"),
    path("members/", include("members.urls")),
]
