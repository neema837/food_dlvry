# Generated by Django 4.2 on 2023-05-25 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0015_alter_menu_idesc'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='cart_status',
            field=models.BooleanField(default=False),
        ),
    ]