# Generated by Django 2.0.4 on 2018-05-06 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tripdiary', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diary',
            name='d_ispublic',
        ),
        migrations.RemoveField(
            model_name='diary',
            name='d_location',
        ),
    ]
