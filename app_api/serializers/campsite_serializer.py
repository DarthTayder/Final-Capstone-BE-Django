from rest_framework import serializers
from app_api.models.campsites import Campsites


class CampsiteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Campsites
        fields = ['id', 'user', 'name', 'address', 'poi']