# Generated by Django 2.2.5 on 2020-06-27 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0007_auto_20200627_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='answer',
            field=models.TextField(blank=True, max_length=10000, null=True),
        ),
    ]
