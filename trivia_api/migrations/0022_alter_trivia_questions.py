# Generated by Django 4.0 on 2022-12-27 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trivia_api', '0021_alter_trivia_questions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trivia',
            name='questions',
            field=models.ManyToManyField(blank=True, to='trivia_api.Question'),
        ),
    ]
