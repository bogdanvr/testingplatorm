# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0003_subuslugi'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subuslugi',
            old_name='usluga',
            new_name='uslugi',
        ),
    ]
