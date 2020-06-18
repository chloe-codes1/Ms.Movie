from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.MovieAPI.as_view()),
    path('recommendation/<user_pk>/', views.MovieRecommendationAPI.as_view()),
    path('<int:movie_id>/', views.MovieDetailAPI.as_view()),
]