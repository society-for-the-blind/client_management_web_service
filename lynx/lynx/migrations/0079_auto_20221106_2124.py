# Generated by Django 2.2.17 on 2022-11-07 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lynx', '0078_auto_20220817_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='status',
            field=models.CharField(blank=True, choices=[('Assigned', 'Assigned'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], default='Assigned', max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='historicalintake',
            name='eye_condition',
            field=models.CharField(blank=True, choices=[('Cataracts', 'Cataracts'), ('Diabetic Retinopathy', 'Diabetic Retinopathy'), ('Glaucoma', 'Glaucoma'), ('Macular Degeneration', 'Macular Degeneration'), ('Other causes of visual impairment', 'Other causes of visual impairment')], max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='intake',
            name='eye_condition',
            field=models.CharField(blank=True, choices=[('Cataracts', 'Cataracts'), ('Diabetic Retinopathy', 'Diabetic Retinopathy'), ('Glaucoma', 'Glaucoma'), ('Macular Degeneration', 'Macular Degeneration'), ('Other causes of visual impairment', 'Other causes of visual impairment')], max_length=250, null=True),
        ),
    ]
