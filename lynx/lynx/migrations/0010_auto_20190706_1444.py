# Generated by Django 2.1.5 on 2019-07-06 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lynx', '0009_progressreport'),
    ]

    operations = [
        migrations.AddField(
            model_name='intake',
            name='pronouns',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='intake',
            name='education',
            field=models.CharField(blank=True, choices=[('None', 'None'), ('GED', 'GED'), ('High School', 'High School'), ('Associates', 'Associates'), ('Bachelors', 'Bachelors'), ('Masters', 'Masters'), ('Doctorate', 'Doctorate')], max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='intake',
            name='ethnicity',
            field=models.CharField(blank=True, choices=[('White', 'White'), ('Hispanic or Latino', 'Hispanic or Latino'), ('Black or African American', 'Black or African American'), ('Asian', 'Asian'), ('American Indian or Alaska Native', 'American Indian or Alaska Native'), ('Native Hawaiian or Other Pacific Islander', 'Native Hawaiian or Other Pacific Islander'), ('Other', 'Other')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='intake',
            name='first_language',
            field=models.CharField(blank=True, choices=[('English', 'English'), ('Armenian', 'Armenian'), ('Arabic', 'Arabic'), ('Bengali', 'Bengali'), ('Cantonese', 'Cantonese'), ('Czech', 'Czech'), ('Danish', 'Danish'), ('Dutch', 'Dutch'), ('Finnish', 'Finnish'), ('French', 'French'), ('German', 'German'), ('Greek', 'Greek'), ('Hebrew', 'Hebrew'), ('Hindi (urdu)', 'Hindi (urdu)'), ('Hmong', 'Hmong'), ('Hungarian', 'Hungarian'), ('Italian', 'Italian'), ('Japanese', 'Japanese'), ('Korean', 'Korean'), ('Lithuanian', 'Lithuanian'), ('Malayalam', 'Malayalam'), ('Mandarin', 'Mandarin'), ('Mon-khmer (cambodian)', 'Mon-khmer (cambodian)'), ('Norwegian', 'Norwegian'), ('Panjabi', 'Panjabi'), ('Persian', 'Persian'), ('Polish', 'Polish'), ('Portuguese', 'Portuguese'), ('Russian', 'Russian'), ('Slovak', 'Slovak'), ('Samoan', 'Samoan'), ('Spanish', 'Spanish'), ('Swahili', 'Swahili'), ('Swedish', 'Swedish'), ('Tagalog', 'Tagalog'), ('Thai (laotian)', 'Thai (laotian)'), ('Turkish', 'Turkish'), ('Ukrainian', 'Ukrainian'), ('Vietnamese', 'Vietnamese')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='intake',
            name='gender',
            field=models.CharField(blank=True, choices=[('Female', 'Female'), ('Male', 'Male'), ('Non-Binary', 'Non-Binary'), ('Gender Non-Conforming', 'Gender Non-Conforming'), ('Other (in notes)', 'Other (in notes)'), ('Prefer Not to Say', 'Prefer Not to Say')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='intake',
            name='second_language',
            field=models.CharField(blank=True, choices=[('English', 'English'), ('Armenian', 'Armenian'), ('Arabic', 'Arabic'), ('Bengali', 'Bengali'), ('Cantonese', 'Cantonese'), ('Czech', 'Czech'), ('Danish', 'Danish'), ('Dutch', 'Dutch'), ('Finnish', 'Finnish'), ('French', 'French'), ('German', 'German'), ('Greek', 'Greek'), ('Hebrew', 'Hebrew'), ('Hindi (urdu)', 'Hindi (urdu)'), ('Hmong', 'Hmong'), ('Hungarian', 'Hungarian'), ('Italian', 'Italian'), ('Japanese', 'Japanese'), ('Korean', 'Korean'), ('Lithuanian', 'Lithuanian'), ('Malayalam', 'Malayalam'), ('Mandarin', 'Mandarin'), ('Mon-khmer (cambodian)', 'Mon-khmer (cambodian)'), ('Norwegian', 'Norwegian'), ('Panjabi', 'Panjabi'), ('Persian', 'Persian'), ('Polish', 'Polish'), ('Portuguese', 'Portuguese'), ('Russian', 'Russian'), ('Slovak', 'Slovak'), ('Samoan', 'Samoan'), ('Spanish', 'Spanish'), ('Swahili', 'Swahili'), ('Swedish', 'Swedish'), ('Tagalog', 'Tagalog'), ('Thai (laotian)', 'Thai (laotian)'), ('Turkish', 'Turkish'), ('Ukrainian', 'Ukrainian'), ('Vietnamese', 'Vietnamese')], max_length=50, null=True),
        ),
    ]
