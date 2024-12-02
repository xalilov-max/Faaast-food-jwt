from rest_framework.routers import DefaultRouter
from .views import FoodTypeViewSet, FoodViewSet, CommentViewSet

router = DefaultRouter()
router.register('food-types', FoodTypeViewSet)
router.register('foods', FoodViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('v1/', include((router.urls, 'v1'))),  
    path('v2/', include((router.urls, 'v2'))),  
