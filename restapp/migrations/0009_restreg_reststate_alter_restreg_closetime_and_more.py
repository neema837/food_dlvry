# Generated by Django 4.2 on 2023-05-15 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0008_restreg_restimg_alter_menu_catid'),
    ]

    operations = [
        migrations.AddField(
            model_name='restreg',
            name='reststate',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='restreg',
            name='closetime',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='restreg',
            name='opentime',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='restreg',
            name='restdist',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='restreg',
            name='restpin',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='restreg',
            name='restplace',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
