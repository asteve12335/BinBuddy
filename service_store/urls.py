from django.urls import path
from . import views

urlpatterns = [
    path('serviceproviders/', views.service_provider_list),
    path('serviceproviders/<int:id>/', views.service_provider_detail),
]
