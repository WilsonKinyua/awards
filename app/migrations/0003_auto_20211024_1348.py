# Generated by Django 3.2.7 on 2021-10-24 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_rate_project_avg_rate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='avg_rate',
        ),
        migrations.AddField(
            model_name='rating',
            name='avg_rate',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
