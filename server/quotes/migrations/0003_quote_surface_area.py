# Generated by Django 4.2.4 on 2023-09-01 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0002_alter_quote_business_name_alter_quote_contact_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='surface_area',
            field=models.IntegerField(default=0),
        ),
    ]
