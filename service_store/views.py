from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import ServiceProvider, Customer
from .serializers import ServiceProviderSerializer, CustomerSerializer

# Create your views here.
class ServiceProviderViewSet(ModelViewSet):
    queryset = ServiceProvider.objects.all()
    serializer_class = ServiceProviderSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class CustomerViewSet(CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    @action(detail=False)
    def me(self, request):
        customer = Customer.objects.get(user_id=request.user.id)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
