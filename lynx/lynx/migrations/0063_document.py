# Generated by Django 2.2.17 on 2021-02-21 21:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import lynx.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lynx', '0062_auto_20210215_1450'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('document', models.FileField(upload_to='documents/')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lynx.Contact')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=models.SET(lynx.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
