from django.shortcuts import render

from rest_framework import viewsets
from .models import testinomials
from .serializer import testinomialsSerializer

# Create your views here.
class testinomialsView(viewsets.ModelViewSet):
    queryset = testinomials.objects.all()
    serializer_class = testinomialsSerializer
    
