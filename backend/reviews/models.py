from django.db import models
from django.contrib.auth import settings
from django_mysql.models import Model
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit

class Review(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True)
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFit(300, 300)],
                                     format='JPEG',
                                     options={'quality': 60})
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    liked_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_reviews')
    # 신고하기
    report = models.ManyToManyField(settings.AUTH_USER_MODEL)


class Comment(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)



    

