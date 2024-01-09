from django.conf import settings
from django.contrib import admin
from django.db import models


class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold'),
    ]

    address = models.CharField(max_length=55, default='Biyem-assi')
    contact = models.CharField(max_length=20,
                               help_text='Enter phone number',
                               default='+237XXXXXXXXX')
    birth_date = models.DateField(null=True)

    membership = models.CharField(max_length=1,
                                  choices=MEMBERSHIP_CHOICES,
                                  default=MEMBERSHIP_BRONZE)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'

    @admin.display(ordering='user__first_name')
    def first_name(self):
        return self.user.first_name

    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name

    def email(self):
        return self.user.email

    class Meta:
        ordering = ['user__first_name', 'user__last_name']


class ServiceProvider(models.Model):
    first_name = models.CharField(max_length=55, default='john')
    last_name = models.CharField(max_length=55, default='Doe')
    username = models.CharField(
        max_length=100, default=f"{first_name} + {last_name}")
    email = models.EmailField(unique=True, default='abc@gmail.com')
    contact = models.CharField(max_length=20,
                               help_text='Enter phone number',
                               default='+237XXXXXXXXX')
    birth_date = models.DateField(null=True)

    company_name = models.CharField(max_length=55, null=True)
    service_area = models.TextField(help_text='Please provide service area(s)')

    def __str__(self) -> str:
        return self.username

    class Meta:
        ordering = ['username']


class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'

    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_FAILED, 'Failed'),
    ]

    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1,
                                      choices=PAYMENT_STATUS_CHOICES,
                                      default=PAYMENT_STATUS_PENDING)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

    class Meta:
        permissions = [
            ('cancel_order', 'Can cancel order')
        ]


class Address(models.Model):
    street = models.TextField(help_text='Please provide popular reference')
    city = models.CharField(max_length=55)
    country = models.CharField(max_length=55)
    customer = models.OneToOneField(
        Customer, on_delete=models.CASCADE, related_name='customer_address', primary_key=True)


class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()


class Garbage(models.Model):
    size = models.PositiveSmallIntegerField(help_text='How many garbage bags?')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    customer = models.OneToOneField(
        Customer, on_delete=models.CASCADE, primary_key=True)
    promotions = models.ManyToManyField(Promotion)


class GarbageCollectionService(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField(
        help_text='How many garbage bags?')
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    service_provider = models.ForeignKey(
        ServiceProvider, on_delete=models.PROTECT)
