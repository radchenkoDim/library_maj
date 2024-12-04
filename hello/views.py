from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def brian(request):
    return HttpResponse("Hello, Brian!")

def dmytro(request):
    return HttpResponse("Hello, Dmytro!")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })