# Generated by Django 4.0.3 on 2024-04-15 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_remove_facturaventa_sesioncaja'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SesionCaja',
        ),
    ]