from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from app_api.models import Reviews, campsites
from app_api.serializers.review_serializer import ReviewsSerializer
from rest_framework.exceptions import ValidationError

class ReviewView(ViewSet):
    def create(self, request):
        
        review= ReviewsSerializer(data=request.data)
        review.is_valid(raise_exception=True)
        review.save()
        
        
        
        return Response(None, status=status.HTTP_201_CREATED)
    
    def list(self, request):
        
        reviews = Reviews.objects.all()
        serializer = ReviewsSerializer(reviews, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk):
        
        reviews = Reviews.objects.get(pk=pk)
        serializer = ReviewsSerializer(reviews)
        return Response(serializer.data)
    
    def destroy(self, request, pk):

        review = Reviews.objects.get(pk=pk)
        review.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        
    
    def update(self, request, pk):
        
        review = Reviews.objects.get(pk=pk)
        review.content = request.data["content"]
        review.campsite_id = request.data["campsite"]
        review.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
