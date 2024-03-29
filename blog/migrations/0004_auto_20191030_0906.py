# Generated by Django 2.2.6 on 2019-10-30 09:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20191030_0903'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='approved_comment',
            new_name='approved_comments',
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 30, 9, 6, 29, 690430, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 30, 9, 6, 29, 689830, tzinfo=utc)),
        ),
    ]
