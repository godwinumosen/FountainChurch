# Generated by Django 5.0.1 on 2024-08-23 12:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fountain', '0010_churchblog'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChurchSermons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sermons_title', models.CharField(blank=True, max_length=255, null=True)),
                ('sermons_description', models.TextField()),
                ('sermons_preach_by', models.CharField(blank=True, max_length=100, null=True)),
                ('sermons_slug', models.SlugField(blank=True, max_length=255, null=True)),
                ('sermons_video', models.FileField(upload_to='videos/')),
                ('sermons_youtube_video_link', models.TextField()),
                ('sermons_publish_date', models.DateTimeField(auto_now_add=True)),
                ('sermons_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-sermons_publish_date'],
            },
        ),
    ]