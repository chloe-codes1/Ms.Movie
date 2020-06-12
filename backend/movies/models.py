from django.db import models, IntegrityError
from django_mysql.models import ListCharField

# API 관련 함수들 API.py에 있어서 import 
import sys
sys.path.insert(0, '../API.py')

import API

# TMDB API
from django.conf import settings
import requests


key = settings.TMDB_API_KEY
# base_url = 'https://api.themoviedb.org/4/list/'
base_url = 'https://api.themoviedb.org/3/discover/movie?'

sort_options = ['release_date.asc', 'release_date.desc', 'original_order.asc', 'original_order.desc',  'vote_average.asc', 'vote_average.desc' ]

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
        

    @classmethod
    def TMDB(cls):
        for page in range(1,50): # Change it to 501 on deployment!
            url = f'{base_url}api_key={key}&language=ko-kr&sort_by=popularity.desc&include_video=false&page={page}'
            response = requests.get(url).json()
            data = response['results']
            for i in range(20):
                try:
                    genre_ids=data[i].get('genre_ids')

                    if Movie.objects.filter(tmdb_id=data[i].get('id')):
                        continue
                
                    Movie.objects.create(
                            title=data[i].get('title'),
                            original_title=data[i].get('original_title'),
                            poster=data[i].get('poster_path'),
                            content=data[i].get('overview'),
                            vote_average=data[i].get('vote_average'),
                            background=data[i].get('backdrop_path'),
                            genres=list( str(API.get_genres(tmdb_id)) for tmdb_id in genre_ids),
                            tmdb_id=data[i].get('id'),
                        )
                except IndexError:
                    break
                except IntegrityError:
                    continue

  
class Cast(models.Model):
    movie = models.ManyToManyField(Movie, related_name='casts', blank=True)
    name = models.CharField(max_length=200)
    department = models.CharField(max_length=100)
    gender = models.IntegerField()
    birthday = models.DateField()
    profile = models.URLField(max_length=200)
    cast_id = models.IntegerField(unique=True)

    def __str__(self):
        return self.name

class Country(models.Model):
    movie = models.ManyToManyField(Movie, related_name='countries', blank=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name