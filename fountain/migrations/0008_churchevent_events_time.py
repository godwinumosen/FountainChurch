# Generated by Django 5.0.1 on 2024-08-21 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fountain', '0007_churchevent'),
    ]

    operations = [
        migrations.AddField(
            model_name='churchevent',
            name='Events_time',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]