# Generated by Django 3.2.8 on 2021-10-22 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_candidate_total_vote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='name',
        ),
        migrations.AddField(
            model_name='candidate',
            name='ketua',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='candidate',
            name='wakil',
            field=models.CharField(default='', max_length=100),
        ),
    ]
