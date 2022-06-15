from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from app_api.models import UserList, campsites
from app_api.serializers.user_list_serializer import UserListSerializer


class UserListView(ViewSet):
    
    def create(self, request):
        
        
        userList= UserListSerializer(data=request.data)
        userList.is_valid(raise_exception=True)
        userList.save()

        return Response(None, status=status.HTTP_201_CREATED)
    
    
    def list(self, request):
        
        userlist = UserList.objects.all()
        serializer = UserListSerializer(userlist, many=True)
        return Response(serializer.data)
    
    
    def retrieve(self, request, pk):
        
        userlist = UserList.objects.get(pk=pk)
        serializer = UserListSerializer(userlist)
        return Response(serializer.data)
    
    
    def destroy(self, request, pk):

        userlist = UserList.objects.get(pk=pk)
        userlist.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        