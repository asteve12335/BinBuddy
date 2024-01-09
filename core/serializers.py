from rest_framework import serializers

class ServiceProviderSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField(max_length=255)
    email = serializers.EmailField()