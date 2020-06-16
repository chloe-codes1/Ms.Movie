from django.db import models, IntegrityError
from django_mysql.models import ListCharField


class Movie(models.Model):
    title = models.CharField(max_length=200)
    original_title = models.CharField(max_length=100)
    poster = models.URLField(max_length=200)
    background = models.URLField(max_length=200)
    vote_average = models.FloatField()
    release_date =models.DateField()
    content = models.TextField()
    tagline = models.CharField(max_length=255)
    runtime = models.IntegerField()
    genres = ListCharField(
        base_field=models.CharField(max_length=10),
        size=6,
        max_length=(6 * 11) 
    )
    tmdb_id = models.IntegerField(unique=True)

    def __str__(self):
        return self.title

  
class Cast(models.Model):
    movie = models.ManyToManyField(Movie, related_name='casts', blank=True)
    name = models.CharField(max_length=200)
    biography=models.TextField()
    department = models.CharField(max_length=100)
    gender = models.IntegerField()
    birthday = models.DateField()
    profile = models.URLField(max_length=200)
    place_of_birth = models.CharField(max_length=255)
    cast_id = models.IntegerField(unique=True)

    def __str__(self):
        return self.name

class Country(models.Model):
    movie = models.ManyToManyField(Movie, related_name='countries', blank=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name