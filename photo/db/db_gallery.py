#coding:utf-8
from photo.db.db import DB
from photo.models import *


class DBGallery(DB):
    def __init__(self):
        super().__init__(Gallery)

    # 基础的查询数据
    def _pack_dict(self,object):
        # print ("store:", object.store , 'customer:' ,object.customer )
        photo_url = object.photo.url if object.photo is not None else ""
        photo_url = photo_url.replace("https://www.51zfgx.com", "http://img.12xiong.top")
        return {
            # "user_id":object.name,
            'gallery_id': object.id,
            "photo_url": photo_url,
             "create_time":object.create_time.strftime("%Y-%m-%d %H:%M:%S"),
        }

if __name__  == '__main__':
    import django
    django.setup()
    # a= DBRelStoreCustomer()
    # print ( a.filter( customer__uuid = '8e6d4c98-63d3-11e9-ad07-b83312f00bac'))
    # a.get_list(customer__uuid = '67e3f912-63d4-11e9-9b5d-b83312f00bac')
    # a.get_list(customer_id = 1)