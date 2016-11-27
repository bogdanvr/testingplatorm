# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField()),
                ('content', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField()),
                ('statement', models.TextField()),
                ('lesson', models.ForeignKey(to='lessons.Lesson')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.TextField()),
                ('status', models.TextField(choices=[('OK', 'Correct'), ('RE', 'Run-time error'), ('WA', 'Wrong answer')])),
                ('info', models.TextField(blank=True)),
                ('time', models.DateTimeField(null=True, auto_now_add=True)),
                ('problem', models.ForeignKey(to='lessons.Problem')),
                ('user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField(unique=True)),
                ('input', models.TextField()),
                ('answer', models.TextField()),
                ('problem', models.ForeignKey(to='lessons.Problem')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
