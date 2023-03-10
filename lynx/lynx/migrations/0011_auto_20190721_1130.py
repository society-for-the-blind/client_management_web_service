# Generated by Django 2.1.5 on 2019-07-21 18:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import lynx.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lynx', '0010_auto_20190706_1444'),
    ]

    operations = [
        migrations.CreateModel(
            name='LessonNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('authorization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lynx.Authorization')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=models.SET(lynx.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='intake',
            name='pronouns',
            field=models.CharField(blank=True, choices=[('He/Him', 'He/Him'), ('She/Her', 'She/Her'), ('They/Them', 'They/Them'), ('Ve/Ver', 'Ve/Ver'), ('Xe/Xim', 'Xe/Xim'), ('Ze/Hir', 'Ze/Hir'), ('Other (in notes)', 'Other (in notes)')], max_length=150, null=True),
        ),
    ]
