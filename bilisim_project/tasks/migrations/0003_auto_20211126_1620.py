# Generated by Django 3.2.9 on 2021-11-26 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_rename_tasks_task'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='excepted_output',
            new_name='expected_output',
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
