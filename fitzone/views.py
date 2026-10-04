from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def programs(request):
    return render(request, "programs.html")


def trainers(request):
    return render(request, "trainers.html")


def contact(request):
    return render(request, "contact.html")
