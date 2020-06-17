from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import ReviewSerializer, ReviewDetailSerializer, ReviewListSerializer, CommentSerializer, ReportSerializer, LikeSerializer, DislikeSerializer
from .models import Review, Comment, Report
from movies.models import Movie
from accounts.models import User
from django.contrib.auth import get_user_model

class ReviewListCreate(APIView):
    def get(self, request, movie_pk):
        movie = get_object_or_404(Movie, id=movie_pk)
        reviews = movie.review_set.order_by('-pk')
        context = { 
            "request":request
        }
        serializer = ReviewListSerializer(reviews, many=True, context=context)
        return Response(serializer.data)

    @permission_classes([IsAuthenticated])
    def post(self, request, movie_pk):
        movie = get_object_or_404(Movie, id=movie_pk)
        user = request.user
        print(user, movie)
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            review = serializer.save(user=user, movie=movie)
            if review:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

      
class ReviewDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(Review, pk=pk)

    def get(self, request, review_pk):
        review = self.get_object(review_pk)
        serializer = ReviewDetailSerializer(review)
        return Response(serializer.data)
    @permission_classes([IsAuthenticated])
    def put(self, request, review_pk):
        review = self.get_object(review_pk)
        print(request)
        print(request.user)
        if review.user == request.user:
            print(review.user)
            print(request.user)
            serializer = ReviewSerializer(review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

          
    @permission_classes([IsAuthenticated])
    def delete(self, request, review_pk):
        review = self.get_object(review_pk)
        if review.user == request.user:
            review.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

# 좋아요 기능

class Like(APIView):
    @permission_classes([IsAuthenticated])
    def put(self, request, review_pk):
        review = get_object_or_404(Review, pk=review_pk)
        user_id = (int(request.data['user']))
        user = User.objects.get(id=user_id)
        print(user)
        print(user.id)
        if review.liked_users.filter(id=user.id).exists():
            review.liked_users.remove(user)
        else:
            review.liked_users.add(user)
        context = {
            'liked_user': review.liked_users,
        }
        serializer = LikeSerializer(review, data=context)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
    
class Dislike(APIView):
    @permission_classes([IsAuthenticated])
    def put(self, request, review_pk):
        review = get_object_or_404(Review, pk=review_pk)
        user_id = (int(request.data['user']))
        user = User.objects.get(id=user_id)
        if review.disliked_users.filter(id=user.id).exists():
            review.disliked_users.remove(user)
        else:
            review.disliked_users.add(user)
        context = {
            'disliked_user': review.disliked_users,
        }
        serializer = DislikeSerializer(review, data=context)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

  
class CommentCreate(APIView):
    @permission_classes([IsAuthenticated])
    def post(self, request, review_pk):
        review = get_object_or_404(Review, pk=review_pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, review=review)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

      
class CommentDetail(APIView):
    def get_comment(self, pk):
        return get_object_or_404(Comment, pk=pk)

    @permission_classes([IsAuthenticated])
    def put(self, request, review_pk, comment_pk):
        comment = self.get_comment(comment_pk)
        if comment.user == request.user:
            serializer = CommentSerializer(comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

          
    @permission_classes([IsAuthenticated])
    def delete(self, request, review_pk, comment_pk):
        comment = self.get_comment(comment_pk)
        if comment.user == request.user:
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

          
# 신고하기
class Reporting(APIView):
    def get(self, request, review_pk):
        reports = Report.objects.filter(review_id=review_pk)
        serializer = ReportSerializer(reports, many=True)
        return Response(serializer.data)

      
    @permission_classes([IsAuthenticated])
    def post(self, request, review_pk):
        review = get_object_or_404(Review, pk=review_pk)
        serializer = ReportSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, review=review)
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

