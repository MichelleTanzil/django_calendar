# Generated by Django 2.2.7 on 2019-11-20 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0003_auto_20191119_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='bg_color',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(),
        ),
    ]
