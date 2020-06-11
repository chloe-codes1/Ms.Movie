from rest_framework import serializers
from .models import Review, Comment
from accounts.serializers import UserSerializer

class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    created_at = serializers.DateTimeField(required=False)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('id', 'user', 'created_at', 'updated_at')

class ReviewListSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username")

    class Meta:
        model = Review
        fields = ('id', 'title', 'user',)


class ReviewDetailSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y년 %m월 %d일 %H:%M:%S")
    user = serializers.CharField(source="user.username")
    class Meta:
        model = Review
        fields = '__all__'


class ReviewReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'title')



class CommentSerializer(serializers.ModelSerializer):
    updated_at = serializers.DateTimeField(required=False)

    class Meta:
        model = Comment
        fields = ('id', 'content', 'user', 'updated_at',)
        read_only_fields = ('id', 'user', 'updated_at',)

