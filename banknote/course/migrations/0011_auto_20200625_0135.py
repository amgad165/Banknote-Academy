# Generated by Django 2.2.5 on 2020-06-25 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0010_auto_20200625_0126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='Start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
