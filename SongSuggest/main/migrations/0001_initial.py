# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-03 01:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('artist', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=20)),
                ('commentary', models.TextField()),
                ('points', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=10)),
                ('admin', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.BooleanField()),
                ('suggestion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Suggestion')),
                ('voter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.User')),
            ],
        ),
        migrations.AddField(
            model_name='suggestion',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='login.User'),
        ),
        migrations.AddField(
            model_name='suggestion',
            name='voters',
            field=models.ManyToManyField(related_name='voters', through='login.Vote', to='login.User'),
        ),
    ]
