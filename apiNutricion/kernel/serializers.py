from rest_framework import serializers, pagination

from kernel.models import Food, User

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ('__all__')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')


class FoodPagination(pagination.PageNumberPagination):
    page_size = 10
    max_page_size = 100


class UserPagination(pagination.PageNumberPagination):
    page_size = 5
    max_page_size = 100