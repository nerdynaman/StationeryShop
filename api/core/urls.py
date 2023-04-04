from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import ProductViewSet, CategoryViewSet, TagViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'tags', TagViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path("", include(router.urls))
]