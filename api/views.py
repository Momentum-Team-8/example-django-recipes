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

    def post(self, request, format=None):
        # we're creating a new recipe with data from the POST request
        # we get that data using request.data
        # check it out in the DRF docs: https://www.django-rest-framework.org/api-guide/requests/#data
        serializer = RecipeSerializer(data=request.data)

        # Now we have to validate this incoming data before we can save it.
        # "When deserializing data, you always need to call is_valid() before attempting to access the validated data, or save an object instance."
        # https://www.django-rest-framework.org/api-guide/serializers/#validation
        if serializer.is_valid():
            serializer.save(user=request.user)
            # ☝️ This is like how we can call form.save() to save the new instance
            # when we wanted to save an associated user, we had to do it in two steps using `commit=False`
            # DRF lets us do it in one clear step without `commit=False`
            return Response(serializer.data)

        # "If any validation errors occur, the .errors property will contain a dictionary representing the resulting error messages."
        # we can use the errors information in our response in case the data is not valid
        return Response(serializer.errors)
