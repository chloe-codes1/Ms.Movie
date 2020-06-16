from django.contrib.auth.models import AbstractUser
from django.db import models
from movies.models import Genre, Movie
import random
import hashlib

class User(AbstractUser):
    GENRE_CHOICE = [
        ('Adventure', 'Adventure'),
        ('Fantasy', 'Fantasy'),
          ('Animation', 'Animation'),
          ('Drama', 'Drama'),
          ('Horror', 'Horror'),
          ('Action', 'Action'),
          ('Comedy', 'Comedy'),
          ('History', 'History'),
          ('Western', 'Western'),
          ('Thriller', 'Thriller'),
          ('Crime', 'Crime'),
          ('Documentary', 'Documentary'),
          ('Science Fiction', 'Science Fiction'),
          ('Mystery', 'Mystery'),
          ('Music', 'Music'),
          ('Romance', 'Romance'),
          ('Family', 'Family'),
          ('War', 'War'),
          ('TV Movie', 'TV Movie'),
        ]
    favorite = models.CharField(max_length=20, choices=GENRE_CHOICE)
    @property
    def gravatar_url(self):
        return f"https://s.gravatar.com/avatar/{hashlib.md5(self.email.encode('utf-8').strip().lower()).hexdigest()}?s=170&d=mp"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)