# Generated by Django 2.2.5 on 2020-06-24 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_auto_20200624_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='Image',
            field=models.URLField(blank=True, default='https://www.abprojeyonetimi.com/wp-content/uploads/2019/09/online-course-development-process-must-know-outsource.jpeg'),
        ),
    ]
