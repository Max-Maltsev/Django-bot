# Generated by Django 4.1.4 on 2023-03-09 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('good', models.CharField(max_length=100)),
                ('prise', models.PositiveIntegerField(max_length=100)),
                ('disc', models.TextField(max_length=1000)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('base_64', models.TextField(blank=True, max_length=300000)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.PositiveIntegerField()),
                ('password', models.TextField(max_length=100)),
                ('many', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
