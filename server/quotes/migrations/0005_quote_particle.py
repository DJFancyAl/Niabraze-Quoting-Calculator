# Generated by Django 4.2.4 on 2023-09-01 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0004_quote_electroless'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='particle',
            field=models.CharField(choices=[('synthetic', 'Synthetic'), ('natural', 'Natural'), ('blend', 'Blend'), ('CBN', 'CBN')], default='synthetic', max_length=20),
        ),
    ]
