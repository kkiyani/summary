# Generated by Django 3.1.5 on 2021-02-04 11:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20210204_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 4, 16, 56, 12, 823024)),
        ),
        migrations.AlterField(
            model_name='employee',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 4, 16, 56, 12, 824025)),
        ),
        migrations.AlterField(
            model_name='historicalemployee',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 4, 16, 56, 12, 824025)),
        ),
    ]
