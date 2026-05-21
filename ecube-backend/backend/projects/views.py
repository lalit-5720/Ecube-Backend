from django.shortcuts import render

from rest_framework import viewsets
from .models import Project
from .serializer import ProjectSerializer

# Create your views here.
class ProjectView(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
