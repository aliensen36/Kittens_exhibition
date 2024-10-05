from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'breeds', BreedViewSet, basename='breed')
router.register(r'kittens', KittenViewSet, basename='kitten')
router.register(r'ratings', KittenRatingViewSet, basename='kitten-rating')

urlpatterns = [
    path('', include(router.urls)),
]
