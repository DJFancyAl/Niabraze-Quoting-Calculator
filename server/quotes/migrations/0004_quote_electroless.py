# Generated by Django 4.2.4 on 2023-09-01 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0003_quote_surface_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='electroless',
            field=models.BooleanField(default=False),
        ),
    ]