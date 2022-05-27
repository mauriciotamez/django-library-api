from django.shortcuts import render
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import  IsAdminUser, IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['title','author','book_id','genre','date_of_publication']
    search_fields = ['title','author','book_id','genre', 'date_of_publication']
    
    def get_permissions(self):
        if self.action == "list":
            permission_classes = [AllowAny]
        elif self.action == "retrieve":
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

 