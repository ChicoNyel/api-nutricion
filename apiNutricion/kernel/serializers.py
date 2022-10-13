from rest_framework import serializers

from kernel.models import Food

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['name', 'calories', 'equivalence', 'measure']