# Generated by Django 5.0a1 on 2023-10-13 20:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_propiedad_googlemaps'),
    ]

    operations = [
        migrations.AddField(
            model_name='propiedad',
            name='precio',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(limit_value=1), django.core.validators.MaxValueValidator(limit_value=999999)]),
        ),
    ]
