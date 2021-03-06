# Generated by Django 4.0.4 on 2022-04-26 00:00

import django.core.validators
from django.db import migrations, models
import jobs.models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='start_date',
            field=models.DateField(validators=[jobs.models.validate_future_date]),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='website',
            field=models.URLField(blank=True, validators=[django.core.validators.URLValidator(schemes=['http', 'https'])]),
        ),
    ]
