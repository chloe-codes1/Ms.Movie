from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth import get_user_model
User = get_user_model()
from .serializers import UserSerializer

# Create your views here.

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

class CreateUserView(CreateModelMixin, GenericViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class UserAPI(APIView):
    def get(self, request):
        print('user api called!')
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

class OtherUserAPI(APIView):
    def get(self, request, user_pk):
        print('other user api called!')
        user = get_object_or_404(User, pk=user_pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

