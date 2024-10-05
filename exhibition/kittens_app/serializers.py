from rest_framework import serializers
from .models import *

class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ['id', 'name']

class KittenSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Kitten
        fields = ['id', 'name', 'color', 'age', 'description', 'breed', 'owner', 'created_at']

class KittenDetailSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    breed = BreedSerializer()

    class Meta:
        model = Kitten
        fields = ['id', 'name', 'color', 'age', 'description', 'breed', 'owner', 'created_at']



class KittenRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = KittenRating
        fields = ['id', 'kitten', 'user', 'rating', 'created_at']
        read_only_fields = ['user', 'created_at']  # Пользователь и дата создания будут заполняться автоматически
