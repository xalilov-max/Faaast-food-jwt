from rest_framework.serializers import ModelSerializer
from .models import FoodType, Food, Comment


class FoodTypeSerializer(ModelSerializer):
    class Meta:
        model = FoodType
        fields = '__all__'


class FoodSerializer(ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
