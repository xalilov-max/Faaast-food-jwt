from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import FoodTypeViewSet, FoodViewSet, CommentViewSet

router = DefaultRouter()
router.register('food-types', FoodTypeViewSet, basename='foodtype')
router.register('foods', FoodViewSet, basename='food')
router.register('comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('v1/', include((router.urls, 'v1'))), 
    path('v2/', include((router.urls, 'v2'))), 
]
