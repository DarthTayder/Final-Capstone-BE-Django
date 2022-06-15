from rest_framework import serializers
from app_api.models.poi import Poi


class PoiSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Poi
        fields = ['id', 'name', ]