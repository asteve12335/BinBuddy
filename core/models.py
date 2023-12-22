from django.db import models


class User(models.Model):
    username = models.CharField(max_length=55)
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    email = models.EmailField(unique=True)
    image = models.ImageField()
    address = models.CharField(max_length=55)
    contact = models.CharField(max_length=20,
                               help_text='Enter phone number')

    def __init__(self, *args, **kwargs):
        """Initializes a user"""
        super().__init__(*args, **kwargs)


class Customer(User, models.Model):
    pass
