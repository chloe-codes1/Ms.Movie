from rest_framework import serializers
from .models import Movie, Cast


class CastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cast
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    
    casts = CastSerializer(many=True)
    countries = serializers.StringRelatedField(many=True)
    genres = serializers.StringRelatedField(many=True)

    class Meta:
        model = Movie
        fields = '__all__'

