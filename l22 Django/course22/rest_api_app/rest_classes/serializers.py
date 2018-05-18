# -*- coding: utf-8 -*-

from rest_framework import serializers

from pizza_auth_app.models import CustomUser
from pizza_app.models import PizzaMenuItem, PizzaIngredient


# class PizzaMenuItemSerializer(serializers.HyperlinkedModelSerializer):
#     """
#     This class is used to get the pizza menu items.
#     But it does not show ingredients.

#     TODO: add ingredients
#     """

#     class Meta:
#         model = PizzaMenuItem
#         fields = ('id', 'name')


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     """
#     This class is used to show users, but favourite_pizza can not be saved.

#     TODO: add possibility to save favourite_pizza
#     """
#     class Meta:
#         model = CustomUser
#         fields = (
#             'id',
#             'username',
#             'email',
#             'our_note',
#             'favourite_pizza',
#         )

#     favourite_pizza = PizzaMenuItemSerializer(required=False)


class PizzaMenuItemSerializer(serializers.ModelSerializer):
    """
    This class is used to get the pizza menu items.
    But it does not show ingredients.

    TODO: add ingredients
    """
    #users = serializers.StringRelatedField(many=True)
    users = serializers.SlugRelatedField(slug_field='username', queryset=CustomUser.objects.all())
    ingredients = serializers.PrimaryKeyRelatedField(many=True, queryset=PizzaIngredient.objects.all())

    
    
    class Meta:
        model = PizzaMenuItem
        fields = ('id', 'name', 'users', 'ingredients')


class UserSerializer(serializers.ModelSerializer):
    """
    This class is used to show users, but favourite_pizza can not be saved.

    TODO: add possibility to save favourite_pizza
    """
    class Meta:
        model = CustomUser
        fields = (
            'id',
            'username',
            'email',
            'our_note',
            'favourite_pizza',
        )

    favourite_pizza = serializers.SlugRelatedField(slug_field='name', queryset=PizzaMenuItem.objects.all())
    
    # def create(self, validated_data):
    #     print ('SELF>>>',self, 'VALIDATED_DATA>>>',validated_data)

    # def update(self, isinstance, validated_data):
    #     print ('>>>>',self, 'INSTANCE>>>',isinstance, validated_data)
