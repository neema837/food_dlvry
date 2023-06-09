# Generated by Django 4.2 on 2023-06-14 01:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("userapp", "0016_order_adrid_alter_checkoutadd_location"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="date",
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="order", name="status", field=models.BooleanField(default=False),
        ),
    ]
