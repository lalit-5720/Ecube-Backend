from rest_framework import serializers
from .models import testinomials

class testinomialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = testinomials
        fields= '__all__'