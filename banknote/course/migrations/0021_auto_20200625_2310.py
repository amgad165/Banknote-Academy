# Generated by Django 2.2.5 on 2020-06-25 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0020_auto_20200625_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='Start_date',
            field=models.DateField(blank=True),
        ),
    ]
