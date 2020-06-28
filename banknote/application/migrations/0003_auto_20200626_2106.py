# Generated by Django 2.2.5 on 2020-06-26 21:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_application_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='Status',
            field=models.CharField(blank=True, default='waiting for apply', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_courses', to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]
