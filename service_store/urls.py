from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('serviceproviders', views.ServiceProviderViewSet)
router.register('customers', views.CustomerViewSet)

urlpatterns = router.urls
