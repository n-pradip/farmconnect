# Generated by Django 5.0.1 on 2024-01-18 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='terms_and_condition',
        ),
    ]