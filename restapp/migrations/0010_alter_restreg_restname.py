# Generated by Django 4.2 on 2023-05-15 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0009_restreg_reststate_alter_restreg_closetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restreg',
            name='restname',
            field=models.CharField(max_length=100),
        ),
    ]