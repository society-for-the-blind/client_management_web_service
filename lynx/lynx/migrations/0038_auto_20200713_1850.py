# Generated by Django 2.1.5 on 2020-07-14 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lynx', '0037_auto_20200712_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
