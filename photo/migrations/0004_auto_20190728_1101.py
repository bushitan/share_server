# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0003_article_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='qr',
        ),
        migrations.RemoveField(
            model_name='article',
            name='type',
        ),
        migrations.AddField(
            model_name='article',
            name='author_logo',
            field=models.CharField(default='', blank=True, max_length=1000, null=True, verbose_name='作者头像'),
        ),
        migrations.AddField(
            model_name='article',
            name='author_name',
            field=models.CharField(default='', blank=True, max_length=100, null=True, verbose_name='作者名字'),
        ),
        migrations.AlterField(
            model_name='article',
            name='cover',
            field=models.CharField(default='', blank=True, max_length=1000, null=True, verbose_name='封面图片'),
        ),
    ]
