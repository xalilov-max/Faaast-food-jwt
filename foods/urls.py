from django.urls import path
from .views import FoodTypeAPIView, FoodAPIView, CommentAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('food-types/', FoodTypeAPIView.as_view(), name='food_types'),
    path('foods/', FoodAPIView.as_view(), name='foods'),
    path('comments/', CommentAPIView.as_view(), name='comments'),
]

urlpatterns += [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]