from django.shortcuts import render
from .models import Project, Skill

def home(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    d={'projects': projects, 'skills': skills}
    return render(request, 'home.html', d)
