# Generated by Django 4.2.4 on 2023-09-07 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0009_alter_quote_difficulty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='surface_area',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
