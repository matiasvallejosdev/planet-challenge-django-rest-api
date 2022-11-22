# Generated by Django 4.1 on 2022-11-22 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_api', '0002_remove_slot_description_slot_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='piece',
            name='description',
        ),
        migrations.AddField(
            model_name='piece',
            name='name',
            field=models.CharField(blank=True, max_length=240),
        ),
    ]
