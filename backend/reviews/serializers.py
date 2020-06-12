from rest_framework import serializers
from .models import Review, Comment
from accounts.serializers import UserSerializer

# create
class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    created_at = serializers.DateTimeField(required=False)

    class Meta:
        model = Review
        fields = ('id', 'title', 'content', 'user', 'created_at', 'updated_at', 'image',)
        read_only_fields = ('id', 'user', 'created_at', 'updated_at')

class ReviewListSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username")

    class Meta:
        model = Review
        fields = ('id', 'title', 'user',)


class ReviewDetailSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField()
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

