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
    context = { "song_data": [1, 2, 3, 4, 5, 6] }
    return render(request, "play.html", context)


def login(request):
    return render(request, "login.html")


def confirm(request):
    username = request.POST["name"]
    password = request.POST["pass"]

    print(f"received username: {username}")
    print(f"received password: {password}")
    
    return render(request, "login.html")
    
