# Generated by Django 5.0.1 on 2024-08-19 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fountain', '0005_rename_fountainchurchtestimony_fountainchurchministerhome_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fountainchurchministerhome',
            name='fountain_church_minister_home_position',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
