# Generated by Django 5.0.11 on 2025-01-17 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_role_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='name',
            field=models.CharField(choices=[(0, 'Manager'), (1, 'User'), (2, 'Publisher'), (3, 'Vip-user')], default=1, max_length=40),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.IntegerField(choices=[(0, 'Manager'), (1, 'User'), (2, 'Publisher'), (3, 'Vip-user')], default=1),
        ),
    ]
