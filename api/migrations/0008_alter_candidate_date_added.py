# Generated by Django 3.2.8 on 2021-11-10 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_candidate_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='date_added',
            field=models.DateField(auto_now_add=True),
        ),
    ]