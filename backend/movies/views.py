from django.conf import settings
from django.shortcuts import get_object_or_404
from django.db import IntegrityError

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status, pagination, generics

from .serializers import MovieSerializer
from .models import Movie, Country, Cast, Genre
from accounts.models import UserProfile

import requests
import random

# API 관련 함수들 API.py에 있어서 import 
import sys
sys.path.insert(0, '../API.py')

import API

from django.contrib.auth import get_user_model
User = get_user_model()

class MovieAPI(APIView):
    
    # GET 요청
    def get(self, request, format=None):
        genre = request.GET.get('genre', None)
        order_by = request.GET.get('order_by', None)
        keyword = request.GET.get('keyword', None)

        movies = Movie.objects.all()
        if genre:
            movies = Movie.objects.filter(genres__name__icontains=genre)
        if order_by:
            option = order_by
            if option == 'Top rating':
                movies = Movie.objects.order_by('-vote_average')
            elif option == 'Latest':
                movies = Movie.objects.order_by('-release_date')
            elif option == 'Oldest':
                movies = Movie.objects.order_by('release_date')
        if keyword:
            movies = Movie.objects.filter(title__icontains=keyword)
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)


    # POST 요청
    def post(self, request, format=None):
        key = settings.TMDB_API_KEY
        base_url = 'https://api.themoviedb.org/3/'
        for page in range(1,501): # Change it to 501 on deployment!
            url = f'{base_url}discover/movie?api_key={key}&sort_by=popularity.desc&include_video=false&page={page}'
            response = requests.get(url).json()
            data = response['results']
            for i in range(20):
                try:
                    genre_ids=data[i].get('genre_ids')
                    tmdb_id=data[i].get('id')

                    if Movie.objects.filter(tmdb_id=tmdb_id):
                        continue

                    genres = []

                    for genre_id in genre_ids:
                        new_genre = str(API.get_genres(genre_id))
                        try:
                            g = Genre.objects.get(name=new_genre)
                        except Genre.DoesNotExist:
                            g = Genre.objects.create(name=new_genre)
                        genres.append(g)                   
                    
                    detail_url = f'{base_url}movie/{tmdb_id}?api_key={key}&append_to_response=credits'
                    
                    detail_response = requests.get(detail_url).json()

                    countries = []

                    try:
                        for country in detail_response.get('production_countries'):
                            try:
                                c = Country.objects.get(name=country.get('name'))
                            except Country.DoesNotExist:
                                c = Country.objects.create(name=country.get('name'))
                            countries.append(c)
                    except TypeError:
                        print('typeerror',detail_url )
                        continue

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
                                        biography = cast_response.get('biography'),
                                        department = cast_response.get('known_for_department'),
                                        gender = cast_response.get('gender'),
                                        birthday = cast_response.get('birthday'),
                                        profile = cast_response.get('profile_path'),
                                        place_of_birth = cast_response.get('place_of_birth'),
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
                            # genres=list( str(API.get_genres(tmdb_id)) for tmdb_id in genre_ids),
                            tmdb_id=tmdb_id,
                        )
                    
                    new_movie.countries.add(*countries)
                    new_movie.casts.add(*casts)
                    new_movie.genres.add(*genres)
                    
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

class MovieRecommendationAPI(APIView):

    def get(self, request, user_pk):
        try:
            user = get_object_or_404(User, id=user_pk)
            recommend_movies = list(Movie.objects.filter(genres__name__icontains=user.userprofile.favorite))
            if len(recommend_movies) < 12:
                recommend_movies += random.sample(list(Movie.objects.all()), 12-len(recommend_movies))
        except UserProfile.DoesNotExist:
            profile = None
            recommend_movies = list(Movie.objects.all())
        recommend_movies = random.sample(recommend_movies, 12)
        
        recommend_movies = random.sample(list(Movie.objects.all()), 12)

        serializer = MovieSerializer(recommend_movies, many=True)
        return Response(serializer.data)



