# Generated by Django 4.2 on 2023-05-05 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0006_rename_type_menu_itype_alter_restreg_restpin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='irate',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
