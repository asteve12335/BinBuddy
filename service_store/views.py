from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ServiceProvider
from .serializers import ServiceProviderSerializer

# Create your views here.


@api_view()
def service_provider_list(request):
    queryset = ServiceProvider.objects.all()
    serializer = ServiceProviderSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view()
def service_provider_detail(request, id):
    service_provider = get_object_or_404(ServiceProvider, pk=id)
    serializer = ServiceProviderSerializer(service_provider)
    return Response(serializer.data)
