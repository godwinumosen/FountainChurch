# Generated by Django 5.0.1 on 2024-08-28 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fountain', '0014_alter_churchgalary_galary_img_pastors'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mainpicture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fountain_first_img', models.ImageField(upload_to='main_img/')),
            ],
        ),
    ]
