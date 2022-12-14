# Generated by Django 4.0 on 2022-12-29 14:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('game_api', '0020_game_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 29, 14, 10, 40, 376955, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 29, 14, 10, 40, 379947, tzinfo=utc), null=True),
        ),
    ]
