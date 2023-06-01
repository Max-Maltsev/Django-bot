# Generated by Django 4.1.4 on 2023-03-14 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_bot_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Call',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.PositiveIntegerField(max_length=10000000)),
                ('prise', models.PositiveIntegerField(max_length=1000)),
                ('name', models.TextField(max_length=1000)),
            ],
        ),
    ]