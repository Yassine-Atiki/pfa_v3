# Generated by Django 5.2 on 2025-04-10 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0008_alter_avi_username_alter_station_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='station',
            name='username',
        ),
    ]
