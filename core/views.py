from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer
from .models import User
from .permissions import UserPermission
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from  rest_framework import status
from bookcase.models import BookItem
from bookcase.serializers import BookItemSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    
    serializer_class = UserSerializer
    queryset =  User.objects.all()

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [AllowAny] 
        elif self.action == 'list':
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [UserPermission]
        return [permission() for permission in permission_classes]
    
    @action(detail=True, permission_classes=[UserPermission])
    def my_books(self, request, pk=None):
        user = User.objects.get(id=pk)
        books = BookItem.objects.filter(current_owner=user)
        self.check_object_permissions(request, user) 
        serializer = BookItemSerializer(books, many=True)
        return Response(serializer.data)
