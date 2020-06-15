from rest_framework import serializers
from .models import Review, Comment, Report, REPORT_REASON
from accounts.serializers import UserSerializer

# create
class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    created_at = serializers.DateTimeField(required=False)
    class Meta:
        model = Review
        fields = ('id', 'title', 'content', 'user', 'created_at', 'updated_at', 'rating', 'movie')
        read_only_fields = ('id', 'user', 'created_at', 'updated_at', 'movie')


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


class ReportSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username")
    review_title = serializers.CharField(source="review.title")
    review_user = serializers.CharField(source="review.user.username")
    reason = serializers.ChoiceField(choices=REPORT_REASON)
    class Meta:
        model = Report
        fields = '__all__'



class CommentSerializer(serializers.ModelSerializer):
    updated_at = serializers.DateTimeField(required=False)
    class Meta:
        model = Comment
        fields = ('id', 'content', 'user', 'updated_at',)
        read_only_fields = ('id', 'user', 'updated_at',)

