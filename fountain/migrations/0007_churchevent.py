# Generated by Django 5.0.1 on 2024-08-21 14:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fountain', '0006_fountainchurchministerhome_fountain_church_minister_home_position'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChurchEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Events_title', models.CharField(blank=True, max_length=255, null=True)),
                ('Events_description', models.TextField()),
                ('Events_slug', models.SlugField(blank=True, max_length=255, null=True)),
                ('Events_img', models.ImageField(upload_to='events_img/')),
                ('Events_date', models.DateTimeField(auto_now_add=True)),
                ('Events_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-Events_date'],
            },
        ),
    ]