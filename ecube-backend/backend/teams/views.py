from django.shortcuts import render

from rest_framework import viewsets
from .models import Team
from .serializer import TeamSerializer

# Create your views here.
class TeamView(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

