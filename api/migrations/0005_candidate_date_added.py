# Generated by Django 3.2.8 on 2021-10-23 12:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20211022_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='date_added',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
