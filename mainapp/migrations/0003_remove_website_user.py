# Generated by Django 3.0.8 on 2020-07-21 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_website'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='website',
            name='user',
        ),
    ]
