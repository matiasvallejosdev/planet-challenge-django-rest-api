# Generated by Django 4.1 on 2022-11-27 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trivia_api', '0006_remove_question_trivia_trivia_questions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trivia',
            name='questions',
        ),
        migrations.AddField(
            model_name='question',
            name='trivia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='trivia_api.trivia'),
        ),
    ]