# Generated by Django 4.1.4 on 2023-03-30 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_bot_app', '0004_users_bonus'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='mail',
            field=models.TextField(blank=True, max_length=1000000),
        ),
        migrations.AddField(
            model_name='users',
            name='nambers',
            field=models.CharField(blank=True, max_length=13),
        ),
    ]