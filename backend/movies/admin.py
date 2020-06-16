from django.contrib import admin
from .models import Movie, Cast, Country, Genre
# Register your models here.

admin.site.register(Movie)
admin.site.register(Cast)
admin.site.register(Country)
admin.site.register(Genre)