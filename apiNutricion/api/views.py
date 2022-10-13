from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.core.handlers.wsgi import WSGIRequest
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from kernel.models import Food
from kernel.serializers import FoodSerializer

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
