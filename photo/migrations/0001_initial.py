# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import photo.models
import lib.image_utils


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=32, verbose_name='名字', null=True, default='', blank=True)),
                ('uuid', models.CharField(max_length=36, verbose_name='uuid', null=True, default='', blank=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', default=django.utils.timezone.now)),
                ('type', models.IntegerField(choices=[(1, '微信公众号'), (2, '小红书'), (3, '实景导航')], verbose_name='类别', default=2)),
                ('title', models.CharField(max_length=100, verbose_name='标题', null=True, default='', blank=True)),
                ('summary', models.CharField(max_length=200, verbose_name='简介', null=True, default='', blank=True)),
                ('description', models.CharField(max_length=500, verbose_name='描述', null=True, default='', blank=True)),
                ('content', models.TextField(verbose_name='内容', null=True, blank=True)),
                ('url', models.CharField(max_length=1000, verbose_name='web地址', null=True, blank=True)),
                ('is_show', models.BooleanField(verbose_name='是否展示', default=True)),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
            },
        ),
        migrations.CreateModel(
            name='BaseImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=32, verbose_name='名字', null=True, default='', blank=True)),
                ('uuid', models.CharField(max_length=36, verbose_name='uuid', null=True, default='', blank=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', default=django.utils.timezone.now)),
                ('url', models.CharField(max_length=1000, verbose_name='云地址', null=True, blank=True)),
                ('local_path', models.ImageField(upload_to=lib.image_utils.ImageUtils.rename, verbose_name='图标', null=True, blank=True)),
                ('type', models.IntegerField(choices=[(1, '封面'), (2, '图标'), (3, '二维码')], verbose_name='类别', default=3)),
            ],
            options={
                'verbose_name': '图库',
                'verbose_name_plural': '图库',
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=32, verbose_name='名字', null=True, default='', blank=True)),
                ('uuid', models.CharField(max_length=36, verbose_name='uuid', null=True, default='', blank=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', default=django.utils.timezone.now)),
                ('is_star', models.BooleanField(verbose_name='收藏', default=False)),
                ('photo', models.ForeignKey(to='photo.BaseImage', verbose_name='文章', null=True, blank=True)),
            ],
            options={
                'verbose_name': '我的照片',
                'verbose_name_plural': '我的照片',
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=32, verbose_name='名字', null=True, default='', blank=True)),
                ('uuid', models.CharField(max_length=36, verbose_name='uuid', null=True, default='', blank=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', default=django.utils.timezone.now)),
                ('article', models.ForeignKey(to='photo.Article', verbose_name='文章', null=True, blank=True)),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
            },
        ),
        migrations.CreateModel(
            name='Prize',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=32, verbose_name='名字', null=True, default='', blank=True)),
                ('uuid', models.CharField(max_length=36, verbose_name='uuid', null=True, default='', blank=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', default=django.utils.timezone.now)),
                ('valid_time', models.DateTimeField(verbose_name='有效期', default=django.utils.timezone.now)),
                ('is_delete', models.BooleanField(verbose_name='是否被删除', default=False)),
            ],
            options={
                'verbose_name': '奖品',
                'verbose_name_plural': '奖品',
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=32, verbose_name='名字', null=True, default='', blank=True)),
                ('uuid', models.CharField(max_length=36, verbose_name='uuid', null=True, default='', blank=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', default=django.utils.timezone.now)),
                ('valid_time', models.DateTimeField(verbose_name='有效期', default=django.utils.timezone.now)),
                ('is_delete', models.BooleanField(verbose_name='是否被删除', default=False)),
                ('is_used', models.BooleanField(verbose_name='是否已使用', default=False)),
                ('exchange_time', models.DateTimeField(verbose_name='礼物兑换时间', default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': '积分',
                'verbose_name_plural': '积分',
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=32, verbose_name='名字', null=True, default='', blank=True)),
                ('uuid', models.CharField(max_length=36, verbose_name='uuid', null=True, default='', blank=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', default=django.utils.timezone.now)),
                ('is_business', models.BooleanField(verbose_name='是否营业', default=True)),
                ('title', models.CharField(max_length=100, verbose_name='标题', null=True, default='', blank=True)),
                ('summary', models.CharField(max_length=200, verbose_name='简介', null=True, default='', blank=True)),
                ('description', models.CharField(max_length=500, verbose_name='描述', null=True, default='', blank=True)),
                ('logo', models.CharField(max_length=500, verbose_name='LOGO', null=True, default='', blank=True)),
                ('share_logo', models.CharField(max_length=500, verbose_name='分享LOGO', null=True, default='', blank=True)),
                ('share_title', models.CharField(max_length=100, verbose_name='分享标题', null=True, default='', blank=True)),
                ('icon', models.CharField(max_length=500, verbose_name='图标', null=True, default='', blank=True)),
                ('phone', models.CharField(max_length=32, verbose_name='电话', null=True, default='', blank=True)),
                ('qr', models.TextField(verbose_name='店铺二维码', null=True, default='', blank=True)),
                ('address', models.CharField(max_length=100, verbose_name='地址', null=True, default='', blank=True)),
                ('latitude', models.FloatField(verbose_name='纬度', null=True, default=0, blank=True)),
                ('longitude', models.FloatField(verbose_name='经度', null=True, default=0, blank=True)),
                ('is_auto', models.BooleanField(verbose_name='是否自助集点', default=False)),
                ('mode', models.IntegerField(choices=[(1, '普通模式'), (2, '分享模式'), (3, '普通分享并行模式')], verbose_name='集点模式', default=1)),
                ('exchange_value', models.IntegerField(verbose_name='兑换礼物点数', default=10)),
                ('check_value', models.IntegerField(verbose_name='普通核销点数', default=1)),
                ('share_check_value', models.IntegerField(verbose_name='分享券核销点数', default=1)),
                ('share_gift_value', models.IntegerField(verbose_name='分享券获赠点数', default=1)),
                ('share_num', models.IntegerField(verbose_name='分享人数', default=1)),
                ('share_limit_time', models.IntegerField(verbose_name='分享券领取时间间隔(天）', default=1)),
                ('share_valid_time', models.IntegerField(verbose_name='分享券有效期(天）', default=1)),
                ('icon_mode', models.IntegerField(choices=[(1, '杯子图案'), (2, '印章图案'), (3, '天梯图案')], verbose_name='图标模式', default=1)),
                ('icon_check_image_url', models.CharField(max_length=500, verbose_name='已集点印章图标', null=True, default='', blank=True)),
                ('icon_un_check_image_url', models.CharField(max_length=500, verbose_name='未集点印章图标', null=True, default='', blank=True)),
                ('icon_full_image_url', models.CharField(max_length=500, verbose_name='集满点印章图标', null=True, default='', blank=True)),
                ('icon_un_full_image_url', models.CharField(max_length=500, verbose_name='未集满点印章图标', null=True, default='', blank=True)),
                ('wm_mode', models.IntegerField(choices=[(1, '普通模式'), (2, '分享模式'), (3, '普通分享并行模式'), (4, '关闭'), (5, '据门票的类别自定义')], verbose_name='外卖模式', default=1)),
                ('wm_check_num', models.IntegerField(verbose_name='发放普通核销点数量', default=1)),
                ('wm_share_num', models.IntegerField(verbose_name='发放分享券数量', default=1)),
                ('start_time', models.DateTimeField(verbose_name='集点开始时间', default=django.utils.timezone.now)),
                ('end_time', models.DateTimeField(verbose_name='集点结束时间', default=photo.models.day_365_hence)),
            ],
            options={
                'verbose_name': '商铺',
                'verbose_name_plural': '商铺',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=32, verbose_name='名字', null=True, default='', blank=True)),
                ('uuid', models.CharField(max_length=36, verbose_name='uuid', null=True, default='', blank=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', default=django.utils.timezone.now)),
                ('name_admin', models.CharField(max_length=32, verbose_name='后台显示名字', null=True, default='', blank=True)),
                ('sort', models.IntegerField(verbose_name='排序', default=0)),
                ('is_top', models.BooleanField(verbose_name='是否置顶', default=False)),
                ('service', models.IntegerField(choices=[(1, '普通模式'), (2, '分享模式'), (3, '普通分享并行模式')], verbose_name='服务状态', default=1)),
                ('is_show', models.BooleanField(verbose_name='是否展示', default=True)),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=32, verbose_name='名字', null=True, default='', blank=True)),
                ('uuid', models.CharField(max_length=36, verbose_name='uuid', null=True, default='', blank=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', default=django.utils.timezone.now)),
                ('nick_name', models.CharField(max_length=100, verbose_name='昵称', null=True, default='', blank=True)),
                ('nick_name_base64', models.TextField(verbose_name='昵称base64', null=True, default='', blank=True)),
                ('avatar_url', models.CharField(max_length=500, verbose_name='头像', null=True, default='', blank=True)),
                ('gender', models.CharField(max_length=100, verbose_name='性别', null=True, default='', blank=True)),
                ('city', models.CharField(max_length=100, verbose_name='城市', null=True, default='', blank=True)),
                ('province', models.CharField(max_length=100, verbose_name='省份', null=True, default='', blank=True)),
                ('country', models.CharField(max_length=100, verbose_name='国家', null=True, default='', blank=True)),
                ('wx_openid', models.CharField(max_length=50, verbose_name='微信OpenID', null=True, default='', blank=True)),
                ('wx_session', models.CharField(max_length=128, verbose_name='微信SessionKey', null=True, default='', blank=True)),
                ('wx_unionid', models.CharField(max_length=50, verbose_name='微信UnionID', null=True, default='', blank=True)),
                ('is_seller', models.BooleanField(verbose_name='是否销售员', default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='score',
            name='customer',
            field=models.ForeignKey(to='photo.User', verbose_name='所属客户', null=True, related_name='customer_score', blank=True),
        ),
        migrations.AddField(
            model_name='score',
            name='delete_seller',
            field=models.ForeignKey(to='photo.User', verbose_name='删除的店员', null=True, related_name='score_delete_seller', blank=True),
        ),
        migrations.AddField(
            model_name='score',
            name='prize',
            field=models.ForeignKey(to='photo.Prize', verbose_name='绑定的奖品', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='score',
            name='seller',
            field=models.ForeignKey(to='photo.User', verbose_name='核销店员', null=True, related_name='seller_score', blank=True),
        ),
        migrations.AddField(
            model_name='score',
            name='store',
            field=models.ForeignKey(to='photo.Store', verbose_name='所属店铺', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='prize',
            name='customer',
            field=models.ForeignKey(to='photo.User', verbose_name='所属客户', null=True, related_name='customer_prize', blank=True),
        ),
        migrations.AddField(
            model_name='prize',
            name='delete_seller',
            field=models.ForeignKey(to='photo.User', verbose_name='删除的店员', null=True, related_name='prize_delete_seller', blank=True),
        ),
        migrations.AddField(
            model_name='prize',
            name='seller',
            field=models.ForeignKey(to='photo.User', verbose_name='核销店员', null=True, related_name='seller_prize', blank=True),
        ),
        migrations.AddField(
            model_name='prize',
            name='store',
            field=models.ForeignKey(to='photo.Store', verbose_name='所属店铺', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(to='photo.User', verbose_name='所属客户', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='gallery',
            name='user',
            field=models.ForeignKey(to='photo.User', verbose_name='所属客户', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='cover',
            field=models.ForeignKey(to='photo.BaseImage', verbose_name='封面图片', null=True, related_name='cover', blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='qr',
            field=models.ForeignKey(to='photo.BaseImage', verbose_name='二维码', null=True, related_name='qr', blank=True),
        ),
    ]
