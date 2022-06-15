from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from app_api.models import Poi
from app_api.serializers.poi_serializer import PoiSerializer

class PoiView(ViewSet):
    def create(self, request):
        
        
        poi= PoiSerializer(data=request.data)
        poi.is_valid(raise_exception=True)
        poi.save()
        
        
        return Response(None, status=status.HTTP_201_CREATED)
        
        
        
    def list(self, request):
        
        poi = Poi.objects.all()
        serializer = PoiSerializer(poi, many=True)
        return Response(serializer.data)
    
    
    def retrieve(self, request, pk):
        
        poi = Poi.objects.get(pk=pk)
        serializer = PoiSerializer(poi)
        return Response(serializer.data)
    
    
    def destroy(self, request, pk):

        poi = Poi.objects.get(pk=pk)
        poi.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        