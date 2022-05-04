# Generated by Django 4.0.4 on 2022-04-27 22:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jokes', '0008_joke_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joke',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='jokes', to='jokes.category'),
        ),
        migrations.AlterField(
            model_name='joke',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='jokes', to='jokes.tag'),
        ),
        migrations.AlterField(
            model_name='joke',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='jokes', to=settings.AUTH_USER_MODEL),
        ),
    ]
