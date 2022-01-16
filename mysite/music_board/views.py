from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, "home.html")



def profile(request):
    return render(request, "profile.html")



def create(request):
    return render(request, "create.html")


def play(request):
    return render(request, "play.html")
