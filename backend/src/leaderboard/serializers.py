from rest_framework import serializers
from .models import UserEntry

#the basic, needed schema or serializer for now
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEntry
        fields = ["id","username","score"]