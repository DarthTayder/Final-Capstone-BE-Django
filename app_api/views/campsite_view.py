
from logging import raiseExceptions
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from app_api.models import Campsites
from app_api.models.poi import Poi
from app_api.serializers.campsite_serializer import CampsiteSerializer
from django.contrib.auth.models import User


class CampsiteView(ViewSet):
    
    def create(self, request):
        # user=User.objects.get(pk=request.auth.user.id)
        # poi=Poi.objects.get(pk=request.data['poi'])
        # request.data[Poi]
        
        camp = CampsiteSerializer(data=request.data)
        camp.is_valid(raise_exception=True)
        camp.save()
            
        
        
        return Response(None, status=status.HTTP_201_CREATED)
    
    
    
    def list(self, request):
        
        campsite = Campsites.objects.all()
        serializer = CampsiteSerializer(campsite, many=True)
        return Response(serializer.data)
    
    
    
    def retrieve(self, request, pk):
        
        campsite = Campsites.objects.get(pk=pk)
        serializer = CampsiteSerializer(campsite)
        return Response(serializer.data)
    
    
    def destroy(self, request, pk):

        campsite = Campsites.objects.get(pk=pk)
        campsite.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        