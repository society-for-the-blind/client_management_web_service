# Generated by Django 2.1.5 on 2019-06-16 18:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import lynx.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lynx', '0006_auto_20190527_1659'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authorization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authorization_number', models.CharField(blank=True, max_length=150, null=True)),
                ('authorization_type', models.CharField(blank=True, choices=[('Hours', 'Hours'), ('Classes', 'Classes')], max_length=25, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('total_time', models.CharField(blank=True, max_length=150, null=True)),
                ('monthly_time', models.CharField(blank=True, max_length=150, null=True)),
                ('billing_rate', models.CharField(blank=True, max_length=150, null=True)),
                ('student_plan', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BillingName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agency', models.CharField(blank=True, max_length=150, null=True)),
                ('cost', models.CharField(blank=True, max_length=50, null=True)),
                ('active', models.BooleanField(blank=True, default=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=models.SET(lynx.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IntakeServiceArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agency', models.CharField(blank=True, max_length=150, null=True)),
                ('active', models.BooleanField(blank=True, default=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=models.SET(lynx.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OutsideAgency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agency', models.CharField(blank=True, max_length=150, null=True)),
                ('contact', models.CharField(blank=True, max_length=150, null=True)),
                ('active', models.BooleanField(blank=True, default=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=models.SET(lynx.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='authorization',
            name='billing_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lynx.BillingName'),
        ),
        migrations.AddField(
            model_name='authorization',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lynx.Contact'),
        ),
        migrations.AddField(
            model_name='authorization',
            name='intake_service_area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lynx.IntakeServiceArea'),
        ),
        migrations.AddField(
            model_name='authorization',
            name='outside_agency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lynx.OutsideAgency'),
        ),
        migrations.AddField(
            model_name='authorization',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.SET(lynx.models.get_sentinel_user), to=settings.AUTH_USER_MODEL),
        ),
    ]
