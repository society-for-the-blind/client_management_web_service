# Generated by Django 2.1.5 on 2020-09-13 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lynx', '0042_auto_20200913_1513'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sipplan',
            name='plan_end',
        ),
        migrations.RemoveField(
            model_name='sipplan',
            name='plan_start',
        ),
    ]