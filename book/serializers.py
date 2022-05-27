from attr import field
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
        depth = 1
        
        extra_kwargs = {
            
            "book_id": {"read_only": True}
        }

    def to_representation(self, data):
        return super(BookSerializer, self).to_representation(data)