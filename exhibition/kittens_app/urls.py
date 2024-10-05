from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'breeds', BreedViewSet, basename='breed')  # Породы
router.register(r'kittens', KittenViewSet, basename='kitten')  # Котята
router.register(r'ratings', KittenRatingViewSet, basename='kitten-rating')  # Оценки котят

urlpatterns = [
    path('', include(router.urls)),  # Включаем маршруты роутера
]
