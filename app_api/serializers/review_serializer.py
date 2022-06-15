from rest_framework import serializers
from app_api.models.reviews import Reviews


class ReviewsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Reviews
        fields = ['id', 'user', 'content', 'campsite']