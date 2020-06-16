from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

# 이걸로 Token key랑 user id 같이 들고온다!
class TokenSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Token
        fields = ('key', 'user')