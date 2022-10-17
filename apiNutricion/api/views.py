from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.core.handlers.wsgi import WSGIRequest

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, RetrieveUpdateAPIView

from kernel.models import Food, User
from kernel.serializers import FoodSerializer, UserSerializer

# Create your views here.

@api_view(['GET'])
def get_food(request: WSGIRequest, arg: str = None) -> Response:
    if arg:
        try:
            food: list = Food.objects.filter(letter=arg)
        except ObjectDoesNotExist:
            food = []
    else:
        food: list = Food.objects.all()
    serializer: FoodSerializer = FoodSerializer(food, many=True)
    return Response(serializer.data)


class UserListApiView(ListAPIView):

    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()


class UserCreateView(CreateAPIView):

    serializer_class = UserSerializer


class UserDetailView(RetrieveAPIView):

    serializer_class = UserSerializer
    queryset = User.objects.filter()


class UserDeleteView(DestroyAPIView):

    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateView(UpdateAPIView):

    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetriveUpdateView(RetrieveUpdateAPIView):

    serializer_class = UserSerializer
    queryset = User.objects.all()
