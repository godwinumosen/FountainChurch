# Generated by Django 5.0.1 on 2024-08-19 22:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fountain', '0003_remove_fountainchurchmainheadimage_fountain_church_slug'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FountainChurchTestimony',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fountain_church_testimony_title', models.CharField(blank=True, max_length=255, null=True)),
                ('fountain_church_testimony_description', models.TextField()),
                ('fountain_church_testimony_img', models.ImageField(upload_to='testy_img/')),
                ('fountain_church_testimony_date', models.DateTimeField(auto_now_add=True)),
                ('fountain_church_testimony_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-fountain_church_testimony_date'],
            },
        ),
    ]