from rest_framework import serializers

from kernel.models import Food, User

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['name', 'calories', 'equivalence', 'measure']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')