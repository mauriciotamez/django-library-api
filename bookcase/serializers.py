import imp
from rest_framework import serializers
from .models import BookItem, Rack
from core.serializers import UserSerializer
from book.serializers import BookSerializer



class RackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rack
        fields = "__all__"

class BookItemSerializer(serializers.ModelSerializer):
    
    current_owner =UserSerializer()
    book = BookSerializer()
    rack = RackSerializer()
    class Meta:
        model = BookItem
        fields = "__all__"
