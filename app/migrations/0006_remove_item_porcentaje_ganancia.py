# Generated by Django 4.0.3 on 2024-04-13 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_anioejercicio_facturaventa_impuesto_item_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='porcentaje_ganancia',
        ),
    ]
