# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_comment_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='imdbId',
            field=models.IntegerField(default=-1),
            preserve_default=False,
        ),
    ]
