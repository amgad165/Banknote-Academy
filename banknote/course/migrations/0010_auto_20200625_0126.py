# Generated by Django 2.2.5 on 2020-06-25 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_course_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='Start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
