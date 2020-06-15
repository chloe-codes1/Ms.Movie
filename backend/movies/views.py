from django.conf import settings
from django.shortcuts import get_object_or_404
from django.db import IntegrityError

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status

from .serializers import MovieSerializer
from .models import Movie, Country, Cast

import requests

# API 관련 함수들 API.py에 있어서 import 
import sys
sys.path.insert(0, '../API.py')

import API

class MovieAPI(APIView):
    
    # GET 요청
    def get(self, request, format=None):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    # POST 요청
    def post(self, request, format=None):
        key = settings.TMDB_API_KEY
        base_url = 'https://api.themoviedb.org/3/'

        for page in range(1,5): # Change it to 501 on deployment!
            url = f'{base_url}discover/movie?api_key={key}&sort_by=popularity.desc&include_video=false&page={page}'
            response = requests.get(url).json()
            data = response['results']
            print('dho..', data)
            for i in range(20):
                try:
                    genre_ids=data[i].get('genre_ids')
                    tmdb_id=data[i].get('id')

                    if Movie.objects.filter(tmdb_id=tmdb_id):
                        continue
                    
                    detail_url = f'{base_url}movie/{tmdb_id}?api_key={key}&append_to_response=credits'
                    detail_response = requests.get(detail_url).json()
                   
                    countries = []
                    
                    for country in detail_response.get('production_countries'):
                        try:
                            c = Country.objects.get(name=country.get('name'))
                        except Country.DoesNotExist:
                            c = Country.objects.create(name=country.get('name'))
                        countries.append(c)
                    
                    casts = []

                    for cast in detail_response.get('credits').get('cast')[:5]:
                        cast_id = cast.get('id')
                        try:
                            c = Cast.objects.get(cast_id=cast_id)
                        except Cast.DoesNotExist:
                            cast_url = f'{base_url}person/{cast_id}?api_key={key}'
                            cast_response = requests.get(cast_url).json()
                            department = cast_response.get('known_for_department')

                            if department == 'Acting':

                                c = Cast.objects.create(
                                        name = cast_response.get('name'),
                                        department = cast_response.get('known_for_department'),
                                        gender = cast_response.get('gender'),
                                        birthday = cast_response.get('birthday'),
                                        profile = cast_response.get('profile_path'),
                                        cast_id = cast_id
                                )
                            else:
                                continue
                        casts.append(c)

                    new_movie = Movie.objects.create(
                            title=data[i].get('title'),
                            original_title=data[i].get('original_title'),
                            poster=data[i].get('poster_path'),
                            content=data[i].get('overview'),
                            vote_average=data[i].get('vote_average'),
                            background=data[i].get('backdrop_path'),
                            release_date=detail_response.get('release_date'),
                            tagline=detail_response.get('tagline'),
                            runtime=detail_response.get('runtime'),
                            genres=list( str(API.get_genres(tmdb_id)) for tmdb_id in genre_ids),
                            tmdb_id=tmdb_id,
                        )
                    
                    new_movie.countries.add(*countries)
                    new_movie.casts.add(*casts)
                except IndexError:
                    break
                except IntegrityError:
                    continue
                except AttributeError:
                    continue
        
        return Response(status=status.HTTP_201_CREATED)

class MovieDetailAPI(APIView):

    def get(self, request, movie_id, format=None):
        movie = get_object_or_404(Movie, pk=movie_id)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
