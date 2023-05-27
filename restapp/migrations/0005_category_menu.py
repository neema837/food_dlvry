# Generated by Django 4.2 on 2023-05-04 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0004_restreg_restrating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catname', models.CharField(max_length=20)),
                ('status', models.BooleanField(default=False)),
                ('restid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapp.restreg')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iname', models.CharField(max_length=20)),
                ('img', models.FileField(upload_to='itemimg')),
                ('iprice', models.IntegerField()),
                ('idesc', models.CharField(max_length=100)),
                ('offer', models.IntegerField()),
                ('preptime', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=20)),
                ('irate', models.IntegerField()),
                ('status', models.BooleanField(default=False)),
                ('catid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapp.category')),
            ],
        ),
    ]