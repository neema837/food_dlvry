# Generated by Django 4.2.1 on 2023-06-07 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0014_rename_udist_userreg_addname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userreg',
            name='upin',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
