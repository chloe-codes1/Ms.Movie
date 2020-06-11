from django.db import models

# TMDB API
from django.conf import settings
import requests

key = settings.TMDB_API_KEY
base_url = 'https://api.themoviedb.org/4/list/'

sort_options = ['release_date.asc', 'release_date.desc', 'original_order.asc', 'original_order.desc',  'vote_average.asc', 'vote_average.desc' ]

class Movie(models.Model):
    title = models.CharField(max_length=100)
    poster = models.URLField(max_length=200)
    background = models.URLField(max_length=200)
    vote_average = models.FloatField()
    content = models.TextField()
    tmdb_id = models.IntegerField()

    @classmethod
    def TMDB(cls, number):
        print(key)
        sort_option = sort_options[number]
        print('sort option?', sort_option)
        for list_id in range(1,11):
            url = f'{base_url}{list_id}?page=1&api_key={key}&sorted_by={sort_option}'
            print(url)
            response = requests.get(url).json()
            data = response['results']
            length = response['total_results']
            print('length?', length)
            for i in range(5):
                Movie.objects.create(
                        title=data[i].get('original_title'),
                        poster=data[i].get('poster_path'),
                        content=data[i].get('overview'),
                        vote_average=data[i].get('vote_average'),
                        background=data[i].get('backdrop_path'),
                        tmdb_id=data[i].get('id'),
                    )