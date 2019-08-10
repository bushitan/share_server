# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0004_auto_20190728_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='like_count',
            field=models.IntegerField(verbose_name='点赞量', default=0),
        ),
    ]
