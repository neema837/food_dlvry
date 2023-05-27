# Generated by Django 4.2 on 2023-05-17 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0014_restreg_joindate'),
        ('userapp', '0003_userreg_joindate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapp.menu')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.userreg')),
            ],
        ),
    ]
