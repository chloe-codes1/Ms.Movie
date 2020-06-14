from django.db import models
from django.contrib.auth import settings
from django_mysql.models import Model
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit

class Review(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True)
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFit(300, 300)],
                                     format='JPEG',
                                     options={'quality': 60})
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

class Report(models.Model):
    REPORT_REASON = [
        ('1', '부적절한 홍보 게시글'),
        ('2', '음란성 또는 청소년에게 부적합한 내용'),
        ('3', '명예훼손 / 사생활 침해 및 저작권침해 등'),
        ('4', '기타'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reporting_reviews', on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    reason = models.CharField(max_length=1, choices=REPORT_REASON)


    

