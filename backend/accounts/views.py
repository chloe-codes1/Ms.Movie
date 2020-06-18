from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from django.contrib.auth import get_user_model
User = get_user_model()
from .serializers import UserSerializer

# Create your views here.

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

from .models import UserProfile


class CreateUserView(CreateModelMixin, GenericViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class UserAPI(APIView):
    def get(self, request):
        print('user api called!')
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def post(self, request, format=None):
        user = request.user
        try:
            UserProfile.objects.get(user = user)
            return Response(status=status.HTTP_409_CONFLICT)
        except UserProfile.DoesNotExist:
            profile = UserProfile.objects.create(
                user = user,
                favorite = request.data.get('favorite')
            )
            return Response(status=status.HTTP_201_CREATED)
            

class OtherUserAPI(APIView):
    def get(self, request, user_pk):
        print('other user api called!')
        user = get_object_or_404(User, pk=user_pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)



# class AuthInfoUpdateView(generics.UpdateAPIView):
#     def put(self, request, user_pk):
#         user = get_object_or_404(User, pk=user_pk)