from rest_framework import serializers
from recipes_app.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe

        # Serialization data
        fields = ['id', 'title', 'description', 'time']
