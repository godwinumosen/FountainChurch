# Generated by Django 5.1.5 on 2025-02-03 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fountain', '0020_remove_churchaudiosermons_audio_sermons_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='churchaudiosermons',
            name='audio_sermons_description',
        ),
        migrations.AddField(
            model_name='churchaudiosermons',
            name='audio_sermons_title',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]
