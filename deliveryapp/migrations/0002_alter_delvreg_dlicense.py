# Generated by Django 4.2 on 2023-04-28 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deliveryapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delvreg',
            name='dlicense',
            field=models.FileField(upload_to='dlicense'),
        ),
    ]
