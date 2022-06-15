import imp
from rest_framework import serializers
from app_api.models.user_list import UserList


class UserListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserList
        fields = ['id', 'user', 'campsiteId']