# Generated by Django 3.2.9 on 2021-11-26 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('problem', models.CharField(max_length=100)),
                ('point', models.FloatField()),
                ('level', models.CharField(max_length=20)),
                ('language', models.CharField(max_length=20)),
                ('input', models.CharField(blank=True, max_length=100)),
                ('excepted_output', models.CharField(max_length=100)),
            ],
        ),
    ]
