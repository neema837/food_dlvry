# Generated by Django 4.2 on 2023-05-15 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0011_menu_restid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='restid',
        ),
    ]