from rest_framework import serializers
from .models import Review, Comment, Report, REPORT_REASON
from accounts.serializers import UserSerializer
from movies.serializers import MovieSerializer


class CommentSerializer(serializers.ModelSerializer):
    updated_at = serializers.DateTimeField(required=False, format="%Y-%m-%d")
    username = serializers.CharField(required=False, source="user.username")
    class Meta:
        model = Comment
        fields = ('id', 'content', 'user', 'updated_at', 'username')
        read_only_fields = ('id', 'user', 'updated_at', 'username')

# create
class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    created_at = serializers.DateTimeField(required=False)
    
    class Meta:
        model = Review
        fields = ('id', 'title', 'content', 'user', 'created_at', 'updated_at', 'rating', 'movie',)
        read_only_fields = ('id', 'user', 'created_at', 'updated_at', 'movie',)


class ReviewListSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username")

    class Meta:
        model = Review
        fields = ('id', 'title', 'user',)


class ReviewDetailSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField(format="%Y-%m-%d")
    username = serializers.CharField(source="user.username")
    movie_title = serializers.CharField(source="movie.title")
    comment_set = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Review
        fields = '__all__'


class ReportSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username")
    review_title = serializers.CharField(source="review.title")
    review_user = serializers.CharField(source="review.user.username")
    reason = serializers.ChoiceField(choices=REPORT_REASON)
    class Meta:
        model = Report
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('liked_users',)

class DislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('disliked_users',)
