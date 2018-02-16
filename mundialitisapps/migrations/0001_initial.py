# Generated by Django 2.0.1 on 2018-02-15 23:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=200)),
                ('score', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Answers',
            },
        ),
        migrations.CreateModel(
            name='lobbies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('players', models.CharField(max_length=200)),
                ('lobpass', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('game', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
            options={
                'verbose_name_plural': 'Trivia Lobbies',
            },
        ),
        migrations.CreateModel(
            name='questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=250)),
                ('option1', models.CharField(max_length=100)),
                ('option2', models.CharField(max_length=100)),
                ('option3', models.CharField(max_length=100)),
                ('option4', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Questions',
            },
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=500)),
                ('password', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'Users',
            },
        ),
    ]
