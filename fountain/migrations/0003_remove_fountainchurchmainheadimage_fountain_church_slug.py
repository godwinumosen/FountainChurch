# Generated by Django 5.0.1 on 2024-08-19 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fountain', '0002_fountainchurchmainheadimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fountainchurchmainheadimage',
            name='fountain_church_slug',
        ),
    ]
