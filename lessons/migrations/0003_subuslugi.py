# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0002_auto_20160703_0846'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubUslugi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(verbose_name='Наименование подуслуги', max_length=20)),
                ('selected', models.BooleanField(verbose_name='Выбранный', default=False, db_index=True)),
                ('usluga', models.ForeignKey(to='lessons.Uslugi')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
