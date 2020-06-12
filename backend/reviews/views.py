from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import ReviewSerializer, ReviewDetailSerializer, ReviewListSerializer, CommentSerializer
from .models import Review, Comment


@api_view(['GET', 'POST'])
def review_list_and_create(request):
    def index(request):
        reviews = Review.objects.all()
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)

    @permission_classes([IsAuthenticated])
    def create(request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data)

    if request.method == 'POST':
        return create(request)
    else:
        return index(request)


@api_view(['GET','PUT', 'PATCH', 'DELETE'])
def review_detail_update_delete(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    def detail(request, review_pk):
        serializer = ReviewDetailSerializer(review)
        return Response(serializer.data)

    @permission_classes([IsAuthenticated])
    def update(request, review_pk):
        if request.user == review.user:
            serializer = ReviewSerializer(review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response(serializer.data)

    @permission_classes([IsAuthenticated])
    def delete(request, review_pk):
        if request.user == review.user:
            review.delete()
        return Response()

    if request.method == 'GET':
        return detail(request, review_pk)
    elif request.method == 'PUT':
        return update(request, review_pk)
    else:
        return delete(request, review_pk)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, review=review)
        return Response(serializer.data)

@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def comment_update_and_delete(request, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)

    def comment_update(request):
        if request.user == comment.user:
            serializer = CommentSerializer(comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response

    def comment_delete(request):
        if request.user == comment.user:
            comment.delete()
        return Response()

    if request.method == 'PUT':
        return comment_update(request)
    else:
        return comment_delete(request)



