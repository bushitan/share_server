#coding:utf-8

from django.db import transaction
from photo.db.db_utils import db
from lib.image_utils import image_utils
from lib.util import *
import time
import datetime

'''
    @method 用户的操作行为
'''
class ActionUser():
    def __init__(self):
        pass


    '''
        普通用户操作
        上传、分享、点赞、助力
    '''


    '''
        @method 用户积分总数
    '''
    def get_count_score(self,user_id):
        return db.score.count_valid(user_id)

    '''
        @method 用户照片表
    '''
    def get_photo_list(self,user_id):
        return db.gallery.get_list(user_id = user_id)

    '''
        @method 七牛token
    '''
    def get_qiniu_token(self,user_id):
        key ,token = image_utils.share_token(user_id)
        return key ,token

    '''
        @method 七牛token
    '''
    def add_photo(self,user_id,image_url):
        count = db.gallery.count(user_id = user_id)
        # 超过10张不能上传
        if count >= USER_MAX_UPLOAD_COUNT:
            return False
        # 上传shiwu
        with transaction.atomic():
            add = db.base_image.add(url = image_url)
            db.gallery.add(user_id = user_id , photo_id = add['id'])
            return True


    '''
        @method 点赞列表
        @return
            like_list 我的点赞列表
    '''
    def get_like_list(self,user_id):
        return db.like.get_my_list( user_id )

    '''
        @method 点赞
    '''
    def add_like(self,user_id,article_id):
        if db.like.is_repeat( user_id , article_id) is True:
            return False
        else:
            db.like.add(user_id = user_id , article_id = article_id)
            return True


    '''
        @method 好友助力
        @param
            user_id 获取积分的用户
            helper_id 帮助好友
    '''
    def add_score(self,customer_id,helper_id):
        if db.score.is_help( customer_id , helper_id) is True:
            return False
        else:
            db.score.add(customer_id = customer_id , helper_id = helper_id)
            return True



    # 店员操作
    # 核销、查询

    '''
        @method 核销
        @param
            seller_uuid
            customer_uuid
    '''
    def seller_check(self,seller_id,customer_id):
        with transaction.atomic():
            db.score.set_used(customer_id)
            # 增加核销记录
            db.prize.add(seller_id = seller_id,customer_id=customer_id )
            return True

    '''
        @method 核销列表
        @param
            seller_uuid
            page_num
            range
        @return
            check_list 核销列表
    '''
    def seller_get_check_prize_list(self,seller_id,page_num,range):
        return db.prize.get_check_list(seller_id,page_num,range )


