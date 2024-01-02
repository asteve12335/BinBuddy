# Generated by Django 5.0 on 2023-12-29 00:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=55)),
                ('first_name', models.CharField(max_length=55)),
                ('last_name', models.CharField(max_length=55)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.CharField(max_length=55)),
                ('contact', models.CharField(help_text='Enter phone number', max_length=20)),
                ('birth_date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('discount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.user')),
                ('membership', models.CharField(choices=[('B', 'Bronze'), ('S', 'Silver'), ('G', 'Gold')], default='B', max_length=1)),
            ],
            bases=('core.user',),
        ),
        migrations.CreateModel(
            name='ServiceProvider',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.user')),
                ('comapny_name', models.CharField(max_length=55, null=True)),
                ('service_area', models.TextField(help_text='Please provide service area(s)')),
            ],
            bases=('core.user',),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('street', models.TextField(help_text='Please provide popular reference')),
                ('city', models.CharField(max_length=55)),
                ('country', models.CharField(max_length=55)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='customer_address', serialize=False, to='core.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placed_at', models.DateTimeField(auto_now_add=True)),
                ('payment_status', models.CharField(choices=[('P', 'Pending'), ('C', 'Complete'), ('F', 'Failed')], default='P', max_length=1)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.customer')),
            ],
        ),
        migrations.CreateModel(
            name='GarbageCollectionService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(help_text='How many garbage bags?')),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.order')),
                ('service_provider', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.serviceprovider')),
            ],
        ),
        migrations.CreateModel(
            name='Garbage',
            fields=[
                ('size', models.PositiveSmallIntegerField(help_text='How many garbage bags?')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='core.customer')),
                ('promotions', models.ManyToManyField(to='core.promotion')),
            ],
        ),
    ]