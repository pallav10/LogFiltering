# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='logdata',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('log_id', models.CharField(max_length=200)),
                ('elapsed_time', models.CharField(max_length=50)),
                ('client_ip', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=400)),
                ('connection_id', models.CharField(max_length=1000)),
                ('date', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=50)),
                ('method_url', models.CharField(max_length=2000)),
                ('http_status', models.CharField(max_length=200)),
                ('byte_transferred', models.CharField(max_length=100)),
                ('referrer_url', models.CharField(max_length=2000)),
                ('user_agent', models.CharField(max_length=500)),
                ('mime', models.CharField(max_length=500)),
                ('filter_name', models.CharField(max_length=500)),
                ('filter_profile', models.CharField(max_length=1000)),
                ('interface', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
