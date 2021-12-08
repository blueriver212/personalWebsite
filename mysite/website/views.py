from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("hello welcome to my website")

def landing(request):
    return render(request, 'base/landing.html')

def about(request):
    return render(request, 'base/about.html')

def projects(request):
    return render(request, 'base/projects.html')

def cv(request):
    return render(request, 'base/cv.html')

def blog(request):
    return render(request, 'base/blog.html')

def movement(request):
    return render(request, 'base/movement.html')
