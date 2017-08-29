# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 09:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pandorastrum', '0019_auto_20170828_1007'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_page_name', models.CharField(blank=True, max_length=100, null=True)),
                ('facebook_link', models.URLField(default='')),
                ('twitter_link', models.URLField(default='')),
                ('twitch_link', models.URLField(default='')),
                ('youtube_link', models.URLField(default='')),
                ('event_date', models.DateField(blank=True, null=True)),
                ('event_description', models.CharField(blank=True, max_length=250, null=True)),
                ('event_image', models.ImageField(blank=True, null=True, upload_to='event')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='gamegenre',
            name='game_genre',
            field=models.CharField(choices=[('MMO', 'Mmo'), ('ACTION', 'Action'), ('SIMULATION', 'Simulation'), ('TRIVIA', 'Trivia'), ('MOBA', 'Moba'), ('PUZZLE', 'Puzzle'), ('FPS', 'Fps'), ('2D', '2D'), ('3RD PERSON', '3rd Person'), ('BEAT EM UP', 'Beat em up'), ('3D', '3d'), ('RPG', 'Rpg'), ('ADVENTURE', 'Adventure'), ('PLATFORMER', 'Platformer'), ('STRATEGY', 'Strategy'), ('ARCADE', 'Arcade'), ('HACK N SLASH', 'Hack n slash'), ('INFINITE RUNNER', 'Infinite Runner'), ('RACING', 'Racing'), ('---', '---'), ('SHOOTING', 'Shooting'), ('SPACE', 'Space'), ('SPORTS', 'Sports')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='portfoliomodel',
            name='category_type',
            field=models.CharField(choices=[('EXPERIMENTAL', 'Experimental'), ('3D', '3d'), ('UNITY', 'Unity'), ('CONCEPT', 'Concept'), ('UNREAL', 'Unreal')], max_length=12),
        ),
    ]