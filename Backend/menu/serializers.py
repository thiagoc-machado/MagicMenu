from rest_framework import serializers
from .models import Menu, Menu_image, Category

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = [
            'name',
            'type',
            'price',
            'description',
            'created_at',
            'updated_at',
            'deleted_at',
            'created_by',
            'updated_by',
            'deleted_by',
            'active',
            'nutrition_score',
            'nutrition_grade',
            'ingredients',
            'allergen',
            'gluten',
            'lactose',
            'allergens',
        ]

class MenuImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu_image
        fields = ['menu', 'image']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['menu', 'name']
