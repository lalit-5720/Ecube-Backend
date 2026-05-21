from django.db import models

# Create your models here.

class testinomials(models.Model):
    name = models.CharField(max_length=100)
    feedback = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return self.name


