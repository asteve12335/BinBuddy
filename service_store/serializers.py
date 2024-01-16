from rest_framework import serializers
from .models import Customer


class GarbageCollectionServiceSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    

class ServiceProviderSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField(max_length=255)
    email = serializers.EmailField()

class CustomerSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()
    class Meta:
        model = Customer
        fields = ['id', 'user_id', 'contact', 'birth_date', 'membership']