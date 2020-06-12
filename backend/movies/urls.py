from django.urls import path
from . import views

urlpatterns = [
    path('', views.MovieAPI.as_view()),
    path('<int:movie_id>/', views.MovieDetailAPI.as_view()),
]