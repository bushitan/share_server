#coding:utf-8
from photo.db.db import DB
from photo.models import *

import datetime
class DBLike(DB):
    def __init__(self):
        super().__init__(Like)

    # 基础的查询数据
    def _pack_dict(self,object):
        _base = super()._pack_dict(object)
        _new = {
            "user_id":object.user_id,
            "article_id":object.article_id,
            # "url":object.url,
            # "qr":object.qr.url if object.qr is not None else "" ,
            #
            #
            # "author_nick_name":object.author.nick_name if object.author is not None else "" ,
            # "author_avatar_url":object.author.avatar_url if object.author is not None else "" ,
        }
        return dict(_base,**_new)

    #点赞列表
    def get_my_list(self,user_id):
        _m = self.model.objects.filter(user_id = user_id,create_time__gte=datetime.datetime.now().date())
        return self._pack_list( self._pack_dict,_m)

    # 是否重复
    def is_repeat(self,user_id,article_id):
        return self.model.objects.filter(user_id = user_id , article_id = article_id , create_time__gte=datetime.datetime.now().date()).exists()




if __name__ == '__main__':
    import django
    django.setup()
    # l = s.get_list()
    # print (l)