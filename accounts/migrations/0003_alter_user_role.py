# Generated by Django 4.2.5 on 2024-01-16 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('Farmer', 'Farmer'), ('Buyer', 'Buyer'), ('Admin', 'Admin')], default='Farmer', max_length=121),
        ),
    ]
