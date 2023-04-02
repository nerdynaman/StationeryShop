from django.contrib import admin
from core.models import Product, Category, Tag, Review
# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Review)