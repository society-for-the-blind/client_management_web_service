# Generated by Django 2.1.5 on 2020-10-21 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lynx', '0051_auto_20201020_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='phone',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
