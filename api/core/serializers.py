from rest_framework import serializers
from core.models import Product, Category, Tag, Review
class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('ProductID', 'CategoryID', 'name', 'cost', 'description', 'discount', 'rating', 'quantity', 'tag1', 'tag2', 'tag3')
        
class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ('CategoryID', 'name')
    
class TagSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tag
        fields = ('TagID', 'TagName')
        
class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = ('ReviewID', 'ProductID', 'rating', 'content')