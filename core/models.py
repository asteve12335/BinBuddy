from django.db import models


class User(models.Model):
    username = models.CharField(max_length=55)
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=55)
    contact = models.CharField(max_length=20,
                               help_text='Enter phone number')
    birth_date = models.DateField(null=True)

    def __init__(self, *args, **kwargs):
        """Initializes a user"""
        super().__init__(*args, **kwargs)


class Customer(User):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold'),
    ]

    membership = models.CharField(max_length=1,
                                  choices=MEMBERSHIP_CHOICES,
                                  default=MEMBERSHIP_BRONZE)


class ServiceProvider(User):
    comapny_name = models.CharField(max_length=55, null=True)
    service_area = models.TextField(help_text='Please provide service area(s)')


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
