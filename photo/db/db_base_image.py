#coding:utf-8
from photo.db.db import DB
from photo.models import *


class DBBaseImage(DB):
    def __init__(self):
        super().__init__(BaseImage)

    # 基础的查询数据
    def _pack_dict(self,object):
        # print ("store:", object.store , 'customer:' ,object.customer )
        _base = super()._pack_dict(object)
        _new = {
            # "id":object.id,
            # 'gallery_id': object.id,
            # "photo_url":object.photo.url if object.photo is not None else "" ,
        }
        return dict(_base,**_new)

if __name__  == '__main__':
    import django
    django.setup()
    # a= DBRelStoreCustomer()
    # print ( a.filter( customer__uuid = '8e6d4c98-63d3-11e9-ad07-b83312f00bac'))
    # a.get_list(customer__uuid = '67e3f912-63d4-11e9-9b5d-b83312f00bac')
    # a.get_list(customer_id = 1)