# Generated by Django 2.1.5 on 2020-10-18 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lynx', '0046_auto_20201011_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='intakenote',
            name='note_type',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
