from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("welcome to the bookstore")

def index(request):
    return render(request, "index.html")


def base(request):
    return render(request, "base.html")

def contact(request):
    return render(request, "contact.html")

def login(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")

def types(request):
    return render(request, "types.html")

def authors(request):
    return render(request, "authors.html")


