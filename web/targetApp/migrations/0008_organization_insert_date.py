# Generated by Django 3.2.4 on 2021-07-07 01:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('targetApp', '0007_auto_20210706_0147'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='insert_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 7, 1, 47, 42, 194559, tzinfo=utc)),
        ),
    ]
