# Generated by Django 4.2.1 on 2024-10-25 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcs',
            name='func',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
    ]
