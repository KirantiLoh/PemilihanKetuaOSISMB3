# Generated by Django 3.2.8 on 2021-11-12 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_candidate_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
