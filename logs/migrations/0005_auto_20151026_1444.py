# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0004_auto_20150929_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logdata',
            name='byte_transferred',
            field=models.FloatField(),
            preserve_default=True,
        ),
    ]
