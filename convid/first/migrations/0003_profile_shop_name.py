# Generated by Django 3.0.3 on 2020-10-19 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0002_profile_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='shop_name',
            field=models.CharField(default='shop name', max_length=300),
        ),
    ]