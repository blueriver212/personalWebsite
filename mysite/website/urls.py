from django.urls import path, include
from . import views


urlpatterns = [
    path('index', views.index, name="index"), # so this would be found at mysite/ >> name will call the view function
    path('', views.landing, name="landing"),
    path('about', views.about, name="about"),
    path('projects', views.projects, name="projects"),
    path('cv', views.cv, name="cv"),
    path('blog', views.blog, name="blog"),
    path('landing', views.landing, name="landing"),
]

