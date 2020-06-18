from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import UserProfile
# from reviews.serializers import ReviewDetailSerializer

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    favorite = serializers.CharField(source='userprofile.favorite')
    # review_set = ReviewDetailSerializer(many=True, read_only=True)                                                                                                         

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password', 'favorite')
        # fields = ('first_name', 'last_name', 'email', 'username', 'password', 'favorite','review_set')

    def create(self, validated_data, instance=None):
        profile_data = validated_data.pop('favorite')


        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        UserProfile.objects.update_or_create(user=user,**profile_data)
        return user

# 이걸로 Token key랑 user id 같이 들고온다!
class TokenSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Token
        fields = ('key', 'user')