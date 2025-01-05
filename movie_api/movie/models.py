from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    release_year = models.IntegerField()
    genre = models.CharField(max_length=255) 
    rating = models.FloatField() 
    # Add other relevant fields like plot, cast, etc.