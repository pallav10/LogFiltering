# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0002_auto_20150929_0507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logdata',
            name='byte_transferred',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
    ]
