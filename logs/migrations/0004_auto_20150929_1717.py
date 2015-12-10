# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0003_auto_20150929_0528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logdata',
            name='byte_transferred',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
