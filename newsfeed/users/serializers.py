from rest_framework import serializers

from .models import User


class UserSerializer(serialziers.ModelSerializer):
    """
    This is the serializer for the User data.
    """
    class Meta:
        model = User
        fields = ('username', 'email', 'name')