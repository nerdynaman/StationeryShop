from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from core.serializers import RecipeSerializer
from core.models import Recipe

class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()