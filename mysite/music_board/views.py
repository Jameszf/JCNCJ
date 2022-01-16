from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello from Music Board!")



def profile(request):
    return HttpResponse("Profile")



def create(request):
    return render(request, "create.html")
