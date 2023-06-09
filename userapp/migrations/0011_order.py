# Generated by Django 4.2 on 2023-06-05 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0010_cart_payment_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderid', models.IntegerField(blank=True, null=True)),
                ('status', models.BooleanField(default=True)),
                ('cartid', models.ManyToManyField(blank=True, null=True, to='userapp.cart')),
                ('userid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='userapp.userreg')),
            ],
        ),
    ]
