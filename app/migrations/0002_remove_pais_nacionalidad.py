# Generated by Django 4.0.3 on 2024-03-15 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pais',
            name='nacionalidad',
        ),
    ]
