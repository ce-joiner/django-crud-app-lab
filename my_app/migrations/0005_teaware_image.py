# Generated by Django 5.2.1 on 2025-05-26 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_teaware'),
    ]

    operations = [
        migrations.AddField(
            model_name='teaware',
            name='image',
            field=models.ImageField(blank=True, upload_to='teaware/'),
        ),
    ]
