# Generated by Django 3.2.5 on 2021-07-10 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('camera_ip', models.CharField(max_length=50)),
                ('capacity', models.IntegerField()),
                ('current_count', models.IntegerField(default=0)),
                ('location', models.CharField(max_length=200)),
                ('other_comments', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
