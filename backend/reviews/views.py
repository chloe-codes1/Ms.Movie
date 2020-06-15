from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import ReviewSerializer, ReviewDetailSerializer, ReviewListSerializer, CommentSerializer, ReportSerializer
from .models import Review, Comment, Report
from movies.models import Movie

class ReviewListCreate(APIView):
    def get(self, request, movie_pk):
        movie = get_object_or_404(Movie, id=movie_pk)
        reviews = movie.review_set
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
        if review.user == request.user:
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
@permission_classes([IsAuthenticated])
def like(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    user = request.user
    is_like = True
    if review.like_users.filter(id=user.id).exists():
        review.like_users.remove(user)
        is_like = False
    else:
        review.like_users.add(user)
    context = {
        'is_like': is_like,
    }
    return JsonResponse(context)

  
# 싫어요 기능
@permission_classes([IsAuthenticated])
def dislike(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    user = request.user
    is_dislike = True
    if review.dislike_users.filter(id=user.id).exists():
        review.dislike_users.remove(user)
        is_dislike = False
    else:
        review.dislike_users.add(user)
    context = {
        'is_dislike': is_dislike,
    }
    return JsonResponse(context)

  
class CommentCreate(APIView):
    @permission_classes([IsAuthenticated])
    def post(self, request, pk):
        review = get_object_or_404(Review, pk=pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, review=review)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

      
class CommentDetail(APIView):
    def get_comment(self, pk):
        return get_object_or_404(Comment, pk=pk)

    @permission_classes([IsAuthenticated])
    def put(self, request, pk):
        comment = self.get_comment(pk)
        if comment.user == request.user:
            serializer = CommentSerializer(comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

          
    @permission_classes([IsAuthenticated])
    def delete(self, request, pk):
        comment = self.get_comment(pk)
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

