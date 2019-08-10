#coding:utf-8
from django.db import models

# Create your models here.
#coding:utf-8
from django.db import models
from lib.util import *
import django.utils.timezone as timezone
def day_365_hence(): #集点默认365天有效期
    return timezone.now() + timezone.timedelta(days=365)
from lib.image_utils import *
from share_server.settings import *
import uuid
# import pymysql
# pymysql.install_as_MySQLdb()

# 基础类 虚函数
class Base(models.Model):
    name = models.CharField(max_length=32, verbose_name=u'名字',default="",null=True,blank=True)
    uuid = models.CharField(max_length=36, verbose_name=u'uuid',default="",null=True,blank=True)
    create_time = models.DateTimeField(u'创建时间',default = timezone.now)
    class Meta:
        abstract = True
    def save(self, *args, **kwargs):
            # 创建用户时，生成唯一ID
            # print (self)
            if not self.uuid:
                self.uuid = str( uuid.uuid1())
            super(Base,self).save(*args, **kwargs)

class BaseImage(Base):
    url = models.CharField(max_length=1000, verbose_name=u'云地址',null=True,blank=True)
    local_path = models.ImageField(u'图标',upload_to=ImageUtils.rename,null=True,blank=True)
    type = models.IntegerField(u'类别',default=BASE_IMAGE_TYPE_QR,choices=BASE_IMAGE_TYPE.items())
    class Meta:
        verbose_name_plural = verbose_name = u'图库'
    def __unicode__(self):
        return '%s' % (self.id)
    def save(self):

        super().save()
        if not self.local_path :
            return

        if not self.url:
            self.url = QINIU_HOST + self.local_path.url
        key = self.local_path.url
        local_file = MEDIA_ROOT+key
        ImageUtils.put(key,local_file)
        super().save()



# 店铺
class Store(Base):
    is_business = models.BooleanField(u'是否营业',default=True)
    title = models.CharField(max_length=100, verbose_name=u'标题',default="",null=True,blank=True)
    summary = models.CharField(max_length=200, verbose_name=u'简介',default="",null=True,blank=True)
    description = models.CharField(max_length=500, verbose_name=u'描述',default="",null=True,blank=True)
    logo = models.CharField(max_length=500, verbose_name=u'LOGO',default="",null=True,blank=True)
    share_logo = models.CharField(max_length=500, verbose_name=u'分享LOGO',default="",null=True,blank=True)
    share_title = models.CharField(max_length=100, verbose_name=u'分享标题',default="",null=True,blank=True)
    icon = models.CharField(max_length=500, verbose_name=u'图标',default="",null=True,blank=True)
    phone =  models.CharField(max_length=32, verbose_name=u'电话',default="",null=True,blank=True)

    qr =  models.TextField(verbose_name=u'店铺二维码',default="",null=True,blank=True)

    address = models.CharField(max_length=100, verbose_name=u'地址',default="",null=True,blank=True)
    latitude =  models.FloatField( verbose_name=u'纬度',default=0,null=True,blank=True)
    longitude =  models.FloatField(  verbose_name=u'经度',default=0,null=True,blank=True)

    is_auto = models.BooleanField(u'是否自助集点',default=False)
    mode = models.IntegerField(u'集点模式',default=STORE_MODE_NORMAL,choices=STORE_MODE.items())
    exchange_value = models.IntegerField(u'兑换礼物点数',default=10)
    check_value = models.IntegerField(u'普通核销点数',default=1)
    share_check_value = models.IntegerField(u'分享券核销点数',default=1)
    share_gift_value = models.IntegerField(u'分享券获赠点数',default=1)
    share_num = models.IntegerField(u'分享人数',default=1)
    share_limit_time = models.IntegerField(u'分享券领取时间间隔(天）',default=1)
    share_valid_time = models.IntegerField(u'分享券有效期(天）',default=1)

    icon_mode = models.IntegerField(u'图标模式',default=STORE_ICON_MODE_CUP,choices=STORE_ICON_MODE.items())
    icon_check_image_url = models.CharField(max_length=500, verbose_name=u'已集点印章图标',default="",null=True,blank=True)
    icon_un_check_image_url = models.CharField(max_length=500, verbose_name=u'未集点印章图标',default="",null=True,blank=True)
    icon_full_image_url = models.CharField(max_length=500, verbose_name=u'集满点印章图标',default="",null=True,blank=True)
    icon_un_full_image_url = models.CharField(max_length=500, verbose_name=u'未集满点印章图标',default="",null=True,blank=True)

    wm_mode = models.IntegerField(u'外卖模式',default=STORE_WM_MODE_NORMAL,choices=STORE_WM_MODE.items())
    wm_check_num =  models.IntegerField(u'发放普通核销点数量',default=1)
    wm_share_num =  models.IntegerField(u'发放分享券数量',default=1)

    start_time = models.DateTimeField(u'集点开始时间',default = timezone.now)
    end_time = models.DateTimeField(u'集点结束时间',default = day_365_hence)

    class Meta:
        verbose_name_plural = verbose_name = u'商铺'
    def __str__(self):

        return '%s' % (self.title )





# 用户 虚函数
class User(Base):
    nick_name =  models.CharField(max_length=100, verbose_name=u'昵称',default="",null=True,blank=True)
    nick_name_base64 =  models.TextField(verbose_name=u'昵称base64',default="",null=True,blank=True)
    avatar_url =  models.CharField(max_length=500, verbose_name=u'头像',default="",null=True,blank=True)
    gender =  models.CharField(max_length=100, verbose_name=u'性别',default="",null=True,blank=True)
    city =  models.CharField(max_length=100, verbose_name=u'城市',default="",null=True,blank=True)
    province =  models.CharField(max_length=100, verbose_name=u'省份',default="",null=True,blank=True)
    country =  models.CharField(max_length=100, verbose_name=u'国家',default="",null=True,blank=True)
    phone =  models.CharField(max_length=100, verbose_name=u'电话',default="",null=True,blank=True)
    # login
    wx_openid = models.CharField(max_length=50, verbose_name=u'微信OpenID',default="",null=True,blank=True)
    wx_session = models.CharField( max_length=128,verbose_name=u'微信SessionKey',default="",null=True,blank=True)
    wx_unionid = models.CharField(max_length=50, verbose_name=u'微信UnionID',default="",null=True,blank=True)

    is_seller =  models.BooleanField(u'是否销售员',default=False)
    class Meta:
        verbose_name_plural = verbose_name = u'人员'
    def __str__(self):
        if self.nick_name != "":
            print( len(self.nick_name ))
            return '%s' % (self.nick_name)
        else:
            return u"ID_%s" % ( self.id)


class Gallery(Base):
    user = models.ForeignKey(User,verbose_name=u'所属客户',null=True,blank=True)
    photo = models.ForeignKey(BaseImage,verbose_name=u'图片',null=True,blank=True)
    is_star = models.BooleanField(u'收藏',default=False)
    class Meta:
        verbose_name_plural = verbose_name = u'我的照片'
        ordering = ['-create_time']
    def __str__(self):
        return '%s' % (self.name)




class DataBase(Base):
    store = models.ForeignKey(Store,verbose_name=u'所属店铺',null=True,blank=True)
    valid_time = models.DateTimeField(u'有效期',default = timezone.now)
    is_delete = models.BooleanField(u'是否被删除',default=False)
    class Meta:
        abstract = True

# 积分
class Score(DataBase):
    is_used= models.BooleanField(u'是否已使用',default=False)
    exchange_time = models.DateTimeField(u'礼物兑换时间',default = timezone.now)
    prize = models.ForeignKey('Prize', verbose_name=u'绑定的奖品',null=True,blank=True)


    seller = models.ForeignKey(User,related_name="seller_score", verbose_name=u'核销店员',null=True,blank=True)
    customer = models.ForeignKey(User,related_name="customer_score",verbose_name=u'所属客户',null=True,blank=True)
    helper = models.ForeignKey(User,related_name="helper",verbose_name=u'助力的客户',null=True,blank=True)

    delete_seller = models.ForeignKey(User, related_name='score_delete_seller',verbose_name=u'删除的店员',null=True,blank=True)
    class Meta:
        verbose_name_plural = verbose_name = u'积分'
        ordering = ['-create_time']
    def __str__(self):
        return '%s' % (self.id)


# 奖品
class Prize(DataBase):
    seller = models.ForeignKey(User,related_name="seller_prize", verbose_name=u'核销店员',null=True,blank=True)
    customer = models.ForeignKey(User,related_name="customer_prize",verbose_name=u'所属客户',null=True,blank=True)
    delete_seller = models.ForeignKey(User, related_name='prize_delete_seller',verbose_name=u'删除的店员',null=True,blank=True)
    class Meta:
        verbose_name_plural = verbose_name = u'奖品'
        # ordering = ['-sn']
        ordering = ['-create_time']
    def __str__(self):
        return '%s' % (self.id)


###############文章###################
class Tag(Base):
    name_admin = models.CharField(max_length=32, verbose_name=u'后台显示名字',default="",null=True,blank=True)
    sort = models.IntegerField(u'排序',default=0)
    is_top = models.BooleanField(u'是否置顶',default=False)
    service = models.IntegerField(u'服务状态',default=STORE_MODE_NORMAL,choices=STORE_MODE.items())
    is_show = models.BooleanField(u'是否展示',default=True)
    class Meta:
        verbose_name_plural = verbose_name = u'标签'
        ordering = ['-sort']
    def __str__(self):
        return '%s' % (self.name )


# 客户
class Article(Base):
    # type = models.IntegerField(u'类别',default=MAP_ARTICLE_TYPE_RED,choices=MAP_ARTICLE_TYPE.items())

    tag = models.ForeignKey(Tag,verbose_name=u'标签',null=True,blank=True)

    # cover = models.ForeignKey(BaseImage, verbose_name=u'封面图片',related_name='cover',null=True,blank=True)
    cover = models.CharField(max_length=1000, verbose_name=u'封面图片',default="",null=True,blank=True)
    title = models.CharField(max_length=100, verbose_name=u'标题',default="",null=True,blank=True)
    summary = models.CharField(max_length=200, verbose_name=u'简介',default="",null=True,blank=True)
    description = models.CharField(max_length=500, verbose_name=u'描述',default="",null=True,blank=True)
    content = models.TextField(verbose_name=u'内容',null=True,blank=True)
    url = models.CharField(max_length=1000, verbose_name=u'web地址',null=True,blank=True)
    # qr = models.ForeignKey(BaseImage, verbose_name=u'二维码',related_name='qr',null=True,blank=True)

    author_logo = models.CharField(max_length=1000, verbose_name=u'作者头像',default="",null=True,blank=True)
    author_name = models.CharField(max_length=100, verbose_name=u'作者名字',default="",null=True,blank=True)
    # author_ = models.CharField(max_length=100, verbose_name=u'标题',default="",null=True,blank=True)

    sn =  models.IntegerField(u'排序',default=0)

    like_count =  models.IntegerField(u'点赞量',default=0)

    is_show = models.BooleanField(u'是否展示',default=True)
    class Meta:
        verbose_name_plural = verbose_name = u'文章'
        ordering = ['-sn']
    def __str__(self):
        return '%s' % (self.id)

class Like(Base):
    user = models.ForeignKey(User,verbose_name=u'所属客户',null=True,blank=True)
    article = models.ForeignKey(Article,verbose_name=u'文章',null=True,blank=True)
    class Meta:
        verbose_name_plural = verbose_name = u'点赞'
    def __str__(self):
        return '%s' % (self.id)
