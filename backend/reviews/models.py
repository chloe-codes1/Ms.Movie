from django.db import models
from django_mysql.models import Model
from django.contrib.auth import settings
from movies.models import Movie

class Review(models.Model):
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    liked_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_reviews', blank=True)
    disliked_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='disliked_reviews', blank=True)

    @property
    def likes(self):
        return self.liked_users.count()
    
    @property
    def dislikes(self):
        return self.disliked_users.count()


class Comment(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)





