# Generated by Django 3.0.3 on 2020-10-26 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0006_profile_checked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(upload_to='img'),
        ),
        migrations.AlterField(
            model_name='section',
            name='img',
            field=models.ImageField(upload_to='img'),
        ),
    ]
