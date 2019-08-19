# -*- coding: utf-8 -*-
from django.contrib import admin
from photo.models import *
from django.utils.safestring import mark_safe
import base64

class BaseAdmin(admin.ModelAdmin):
	readonly_fields = ("uuid",)
	list_per_page = 20


class StoreAdmin(BaseAdmin):
	list_display = ('id','name',)
    # list_per_page = BaseAdmin.list_per_page
admin.site.register(Store,StoreAdmin)

class BaseImageAdmin(admin.ModelAdmin):
	list_display = ('id','url_image','url','local_path','type',)
	def url_image(self, obj):
		return  mark_safe('<img src="%s" width="50px" />' % (obj.url))
	url_image.short_description = u'图片'
	url_image.allow_tags = True
admin.site.register(BaseImage,BaseImageAdmin)


class UserAdmin(BaseAdmin):
	list_display = ('id','name','is_seller','nick_name','name_base64','uuid','wx_openid',)
	fieldsets = (
        (u"客户属性", {'fields': ['uuid','name','nick_name_base64','is_seller']}),
		(u"微信数据", {'fields': ['nick_name','avatar_url','gender','city','province','country','phone',]}),
		(u"系统数据", {'fields': ['wx_openid','wx_session','wx_unionid',]}),
    )
	search_fields = ('id','wx_openid','uuid',)

	def name_base64(self, obj):
		return  str(base64.b64decode(obj.nick_name_base64),'utf-8')
	name_base64.short_description = u'昵称64编码'
	name_base64.allow_tags = True
	readonly_fields = ("uuid",'wx_openid','wx_session','wx_unionid','name_base64',)
admin.site.register(User,UserAdmin)


class GalleryAdmin(BaseAdmin):
	list_display = ['id','user','get_name','get_phone','logo_image','is_star',]
    # fieldsets = (
    #     (u"关系", {'fields': ['store','customer',]}),
    # )
	search_fields = ('id',)
	def get_name(self, obj):
		# print(obj.user_id)
		if  obj.user is not None:
			return  obj.user.name
		else:
			return ""
	get_name.short_description = '用户名称'
	def get_phone(self, obj):
		if  obj.user is not None:
			return obj.user.phone
		else:
			return ""
	get_phone.short_description = '用户电话'
	# 分享二维码的展示图片
	def logo_image(self, obj):
		if obj.photo is not None:
			photo_url = obj.photo.url
			photo_url = photo_url.replace("https://www.51zfgx.com", "http://img.12xiong.top")
			return  mark_safe('<img src="%s?imageView2/1/w/96/h/96" name="%s" width="50px"  onclick="javascript:window.open(this.name)"/>' % (photo_url,photo_url))
		else:
			return  mark_safe('<img src="" width="50px" />' )
	logo_image.short_description = u'上传图片'
	logo_image.allow_tags = True
	list_editable = ("is_star",)
	list_filter = ("is_star",)
	readonly_fields = ("get_name","get_phone","logo_image",)

admin.site.register(Gallery,GalleryAdmin)




class ScoreAdmin(BaseAdmin):
	list_display = ('id','is_used','store_id','seller_id','customer_id','helper','exchange_time','is_delete','create_time',)
	fieldsets = (
        (u"公共数据", {'fields': ['is_used','exchange_time','create_time',]}),
        (u"集点数据", {'fields': ['store','seller','customer','helper',]}),
        (u" 删除状态", {'fields': ['is_delete','delete_seller',]}),
        # (u"分享积分", {'fields': ['share',]}),
    )
	search_fields = ('id',)
admin.site.register(Score,ScoreAdmin)


class PrizeAdmin(BaseAdmin):
	list_display = ('id','store_id','seller_id','customer_id','is_delete','create_time',)
	fieldsets = (
        (u"兑换", {'fields': ['store','customer','seller',]}),
        (u" 删除状态", {'fields': ['is_delete','delete_seller',]}),
    )
	search_fields = ('id',)
admin.site.register(Prize,PrizeAdmin)



class LikeAdmin(BaseAdmin):
	list_display = ('id','user','article')
admin.site.register(Like,LikeAdmin)


###############we文章###################

class MapAdmin(BaseAdmin):
	list_display = ('id','name_admin','name','service','is_top','sort',)
	fieldsets = (
        (u"名称", {'fields': ['uuid','name','name_admin','is_show',]}),
        (u"归属", {'fields': ['service',]}),
		(u"内容", {'fields': ['is_top','service','sort',]}),
    )
	# raw_id_fields = ("father",)
admin.site.register(Tag,MapAdmin)


class ArticleAdmin(BaseAdmin):
	list_display = ('id','title','author_name','tag','sn','like_count',)
	fieldsets = (
		(u"作者", {'fields': ['is_show','author_logo','author_name','sn','like_count',]}),
		(u"内容", {'fields': ['tag','cover','title','url',]}),
	)
	list_editable = ('sn','like_count',)
	# search_fields = ('poi__name',)
	# list_filter = ('author', )
	# raw_id_fields = ("poi",'cover','qr','author',)
    #
	def cover_image(self, obj):
		if obj.cover is not None:
			return  mark_safe('<img src="%s" width="50px" />' % (obj.cover))
		else:
			return  mark_safe('<img src="" width="50px" />' )
	cover_image.short_description = u'封面'
	cover_image.allow_tags = True

	# 分享二维码的展示图片
	def logo_image(self, obj):
		if obj.author_logo is not None:
			author_logo = obj.author_logo
			author_logo = author_logo.replace("https://www.51zfgx.com", "http://img.12xiong.top")
			return  mark_safe('<img src="%s?imageView2/1/w/96/h/96" name="%s" width="50px"  onclick="javascript:window.open(this.name)"/>' % (author_logo,author_logo))
		else:
			return  mark_safe('<img src="" width="50px" />' )
	logo_image.short_description = u'作者头像'
	logo_image.allow_tags = True
	readonly_fields = ("cover_image","logo_image",)
admin.site.register(Article,ArticleAdmin)
