# Generated by Django 3.2.5 on 2021-07-12 05:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flowControl', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='camera_ip',
            new_name='camera_ip_url',
        ),
    ]