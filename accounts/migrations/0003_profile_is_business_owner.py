# Generated by Django 5.0.6 on 2024-06-23 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_profile_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_business_owner',
            field=models.BooleanField(default=False),
        ),
    ]
