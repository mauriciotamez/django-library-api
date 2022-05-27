from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "password", "first_name",
                  "last_name", "id", "date_joined", "last_login","rented_books")
                  
        extra_kwargs = {
            "password": {"write_only": True},
            "id": {"read_only": True},
            "date_joined": {"read_only": True},
            "last_login": {"read_only": True},
            "rented_books": {"read_only": True}
        }

    def create(self, validated_data):
        user = User(
            **validated_data
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
    
    def to_representation(self, data):
        return super(UserSerializer, self).to_representation(data)