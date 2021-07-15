from django.shortcuts import render
from api.serializers import RecipeSerializer
from recipes.models import Recipe
from rest_framework.views import APIView
from rest_framework.response import Response


class RecipeListView(APIView):
    """
    List all recipes
    """

    def get(self, request, format=None):
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)
