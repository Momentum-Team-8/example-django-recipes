from rest_framework import serializers
from recipes.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    tags = serializers.SlugRelatedField(many=True, read_only=True, slug_field="tag")

    class Meta:
        model = Recipe
        fields = (
            "pk",
            "user",
            "title",
            "prep_time_in_minutes",
            "cook_time_in_minutes",
            "tags",
            "public",
        )
