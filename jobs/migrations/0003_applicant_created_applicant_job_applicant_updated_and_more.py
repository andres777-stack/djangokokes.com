# Generated by Django 4.0.4 on 2022-04-26 03:41

from django.db import migrations, models
import django.db.models.deletion
import jobs.models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_alter_applicant_start_date_alter_applicant_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='applicant',
            name='job',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='jobs.job'),
        ),
        migrations.AddField(
            model_name='applicant',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='available_days',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='desired_hourly_wage',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='email',
            field=models.EmailField(help_text='A valid email address', max_length=254),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='start_date',
            field=models.DateField(help_text='The earliest date you can start working', validators=[jobs.models.validate_future_date]),
        ),
    ]
