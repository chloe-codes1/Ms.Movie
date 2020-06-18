from django.contrib.auth.models import AbstractUser
from django.db import models

# from django.dispatch import receiver
# from django.db.models.signals import post_save

# import random
# import hashlib

from django_mysql.models import ListCharField 

class User(AbstractUser):
    pass
    # GENRE_CHOICE = [
    #     ('Adventure', 'Adventure'),
    #     ('Fantasy', 'Fantasy'),
    #       ('Animation', 'Animation'),
    #       ('Drama', 'Drama'),
    #       ('Horror', 'Horror'),
    #       ('Action', 'Action'),
    #       ('Comedy', 'Comedy'),
    #       ('History', 'History'),
    #       ('Western', 'Western'),
    #       ('Thriller', 'Thriller'),
    #       ('Crime', 'Crime'),
    #       ('Documentary', 'Documentary'),
    #       ('Science Fiction', 'Science Fiction'),
    #       ('Mystery', 'Mystery'),
    #       ('Music', 'Music'),
    #       ('Romance', 'Romance'),
    #       ('Family', 'Family'),
    #       ('War', 'War'),
    #       ('TV Movie', 'TV Movie'),
    #     ]
    # favorite = models.CharField(max_length=20, choices=GENRE_CHOICE)
    
    # favorite = models.CharField(blank=True, max_length=20)
    # @property
    # def gravatar_url(self):
    #     return f"https://s.gravatar.com/avatar/{hashlib.md5(self.email.encode('utf-8').strip().lower()).hexdigest()}?s=170&d=mp"

    # @receiver(post_save, sender=User)
    # def create_user_profile(self, instance, created, **kwargs):
    #     if created:
    #         User.objects.create(user=instance)

    # @receiver(post_save, sender=User)
    # def save_user_profile(self, instance, **kwargs):
    #     instance.profile.save()
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    favorite = models.CharField(max_length=200)
    # favorites = ListCharField(
    #     base_field=models.CharField(max_length=10),
    #     size=6,
    #     max_length=(6 * 11) 
    # )


    # userprofile.favorite