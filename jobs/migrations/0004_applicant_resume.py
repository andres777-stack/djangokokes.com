# Generated by Django 4.0.4 on 2022-04-27 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_applicant_created_applicant_job_applicant_updated_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='resume',
            field=models.FileField(blank=True, help_text='PDF only', upload_to='private/resumes'),
        ),
    ]
