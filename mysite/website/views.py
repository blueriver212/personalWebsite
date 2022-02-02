from mmap import PAGESIZE
from django.shortcuts import render
from django.http import HttpResponse
import os
from django.conf import settings


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
    filepath = os.path.join(settings.STATIC_ROOT, 'images\\Indigo_Brownhall_CV.pdf')
    with open(filepath, 'rb') as pdf:
        response = HttpResponse(pdf.read(),content_type='application/pdf')
        response['Content-Disposition'] = 'filename=Indigo_Brownhall.pdf'
        return response

def blog(request):
    return render(request, 'base/blog.html')

def movement(request):
    return render(request, 'base/movement.html')


# Generate a PDF File Venue List using reportlab

