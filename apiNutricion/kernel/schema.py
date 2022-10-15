import graphene
from graphene_django import DjangoObjectType
from .models import *

class FoodType(DjangoObjectType):
    class Meta:
        model = Food


class Query(graphene.ObjectType):
    all_foods = graphene.List(FoodType)
    food_by_letter = graphene.List(FoodType, letter=graphene.String(required=True))
    food_by_name = graphene.Field(FoodType, name=graphene.String(required=True))

    def resolve_all_foods(root, info):
        return Food.objects.all()
        

    def resolve_food_by_letter(root, info, letter):
        listFoods = Food.objects.filter(letter=letter)
        if len(listFoods) == 0:
            return []
        else:
            return listFoods


    def resolve_food_by_name(root, info, name):
        try:
            return Food.objects.get(name=name)
        except Food.DoesNotExist:
            return None