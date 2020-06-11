from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import ReviewSerializer, ReviewDetailSerializer, ReviewListSerializer
from .models import Review, Comment


@api_view(['GET', 'POST'])
def review_list_and_create(request):
    def index(request):
        reviews = Review.objects.all()
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)

# @permission_classes([IsAuthenticated])
def create(request):
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data)

    if request.method == 'POST':
        return create(request)
    else:
        return index(request)


@api_view(['GET','PUT','DELETE'])
def review_detail_update_delete(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    def detail(request, review_pk):
        serializer = ReviewDetailSerializer(review)
        return Response(serializer.data)

    # @permission_classes([IsAuthenticated])
    def update(request, review_pk):
        # if request.user == review.user:
        serializer = ReviewSerializer(review)




    # @permission_classes([IsAuthenticated])
    def delete(request, review_pk):
        # if request.user == review.user:
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
def comment_create(request):
    pass
