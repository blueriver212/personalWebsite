from mmap import PAGESIZE
from django.shortcuts import render
from django.http import HttpResponse

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


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
    with open("C:/Users/someg/OneDrive/Documents/PhD_application/Indigo_Brownhall_CV.pdf", 'rb') as pdf:
        response = HttpResponse(pdf.read(),content_type='application/pdf')
        response['Content-Disposition'] = 'filename=Indigo_Brownhall.pdf'
        return response

def blog(request):
    return render(request, 'base/blog.html')

def movement(request):
    return render(request, 'base/movement.html')


# Generate a PDF File Venue List using reportlab

