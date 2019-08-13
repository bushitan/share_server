#coding:utf-8

from photo.message.message_utils import message
from photo.db.db_utils import db

'''
    @class 业务权限检测
'''
class Detection():
    def __init__(self):
        # TODO 初始化action
        pass

    @staticmethod
    def base(func):
        def wrapper(self,request,*args, **kwargs):
            print ("base 1234")
            return func(self,request,*args, **kwargs)
        return wrapper

    '''
        @method 检测用户存在
    '''
    def user_exist(self,func):
        @Detection.base
        def wrapper(self,request,*args, **kwargs):
            #TODO 使用action判断，跟view同一级别
            print ("user_login")
            return func(self,request,*args, **kwargs)
        return wrapper

    '''
        @method 检测用户
    '''
    def user(self,func):
        @Detection.base
        def wrapper(self,request,*args, **kwargs):
            uuid = request.POST.get('uuid','')
            # 检测用户是否存在
            if db.user.is_exists(uuid = uuid) is False:
                return {
                    'message':message.user_none()
                }
            # 将uuid转为user_id
            kwargs['user_id'] = db.user.get(uuid = uuid).id
            return func(self,request,*args, **kwargs)
        return wrapper

    '''
        @method 扫码检测
    '''
    def scan(self,func):
        @Detection.base
        def wrapper(self,request,*args, **kwargs):
            customer_id = request.POST.get('customer_id','')
            # 检测用户是否存在
            if db.user.is_exists(id = customer_id) is False:
                return {
                    'message':message.user_customer_none()
                }
            # 将uuid转为user_id
            kwargs['customer_id'] = customer_id
            return func(self,request,*args, **kwargs)
        return wrapper


    def article_exist(self,func):
        @Detection.base
        def wrapper(self,request,*args, **kwargs):
            article_id = request.POST.get('article_id',"")
            if article_id == "":
                 return {
                    'message': message.article_none()
                }
            if db.article.is_exists(id = article_id ) is False:
                return {
                    'message': message.article_none()
                }
            return func(self,request,*args, **kwargs)
        return wrapper

    # 图片上传为空
    def image_url_none(self,func):
        @Detection.base
        def wrapper(self,request,*args, **kwargs):
            image_url = request.POST.get('image_url',"")
            if image_url == "":
                 return {
                    'message': message.user_customer_image_none()
                }
            return func(self,request,*args, **kwargs)
        return wrapper


detection = Detection()