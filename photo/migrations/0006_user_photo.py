# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0005_article_like_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.CharField(max_length=100, blank=True, default='', null=True, verbose_name='电话'),
        ),
    ]
