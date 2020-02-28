# Generated by Django 2.1.5 on 2019-10-06 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lynx', '0020_auto_20191006_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='intake',
            name='alzheimers',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='intake',
            name='arthritis',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='intake',
            name='employment_goals',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='intake',
            name='hobbies',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='intake',
            name='musculoskeletal',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='intake',
            name='degree',
            field=models.CharField(blank=True, choices=[('Totally Blind (NP or NLP)', 'Totally Blind (NP or NLP)'), ('Legally Blind', 'Legally Blind'), ('Severe Visual Impairment', 'Severe Visual Impairment'), ('Low Vision', 'Low Vision')], max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='intake',
            name='prognosis',
            field=models.CharField(blank=True, choices=[('Stable', 'Stable'), ('Diminishing', 'Diminishing')], max_length=250, null=True),
        ),
    ]