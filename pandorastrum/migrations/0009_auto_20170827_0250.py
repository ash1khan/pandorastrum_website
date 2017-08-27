# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-26 20:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pandorastrum', '0008_auto_20170827_0223'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamesmodel',
            name='android',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='gamesmodel',
            name='console',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='gamesmodel',
            name='pc',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='gamesmodel',
            name='web',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='gamegenre',
            name='game_genre',
            field=models.CharField(choices=[('RPG', 'Rpg'), ('MOBA', 'Moba'), ('---', '---'), ('PLATFORMER', 'Platformer'), ('MMO', 'Mmo'), ('STRATEGY', 'Strategy'), ('SIMULATION', 'Simulation'), ('ADVENTURE', 'Adventure'), ('RACING', 'Racing'), ('3RD PERSON', '3rd Person'), ('ARCADE', 'Arcade'), ('PUZZLE', 'Puzzle'), ('3D', '3d'), ('BEAT EM UP', 'Beat em up'), ('FPS', 'Fps'), ('INFINITE RUNNER', 'Infinite Runner'), ('ACTION', 'Action'), ('SPORTS', 'Sports'), ('2D', '2D'), ('TRIVIA', 'Trivia'), ('SPACE', 'Space'), ('SHOOTING', 'Shooting'), ('HACK N SLASH', 'Hack n slash')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='portfoliomodel',
            name='category_type',
            field=models.CharField(choices=[('CONCEPT', 'Concept'), ('UNREAL', 'Unreal'), ('3D', '3d'), ('EXPERIMENTAL', 'Experimental'), ('UNITY', 'Unity')], max_length=12),
        ),
    ]
