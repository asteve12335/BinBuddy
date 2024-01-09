from django.contrib import admin
from django.utils.html import format_html
from . import models


@admin.register(models.ServiceProvider)
class ServiceProviderAdmin(admin.ModelAdmin):
    list_display = ['username', 'company_name',
                    'service_area', 'email', 'contact']
    list_editable = ['service_area']
    ordering = ['first_name', 'last_name']
    list_per_page = 10


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership', 'contact', 'email']
    list_editable = ['membership']
    list_select_related = ['user']
    ordering = ['user__first_name', 'user__last_name']
    list_per_page = 20
    search_fields = ['first_name__istartswith', 'last_name__istartswith']


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'placed_at', 'payment_status']
    list_editable = ['payment_status']
    list_per_page = 10


# Register your models here.
