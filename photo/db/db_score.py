#coding:utf-8
from photo.db.db import DBData
from photo.db.db_store import DBStore
from photo.models import *


class DBScore(DBData):
    def __init__(self):
        super().__init__(Score)

    # 基础的查询数据
    def _pack_dict(self,object):
        _base = super()._pack_dict(object)
        _new = {
            "is_used":object.is_used,
            "exchange_time":object.exchange_time.strftime("%Y-%m-%d %H:%M:%S"),
        }
        return dict(_base,**_new)


    '''
        @method 可以使用的积分
    '''
    def count_valid(self,customer_id):
        # user = self.model.objects.get(uuid = uuid )
        return self.model.objects.filter(
            customer_id = customer_id ,
            is_used = False
    #         store = store,
    #         customer__uuid = customer_uuid,
    #         is_used = False,
    #         is_delete = False,
    #         create_time__gt = store.start_time,
    #         create_time__lt = store.end_time,
        ).count()

    '''
        @method 可以使用的积分
    '''
    def set_used(self,customer_id):
        self.model.objects.filter(
            customer_id = customer_id ,
            is_used = False
        ).update( is_used = True )
        return True

    # 是否已经助力
    def is_help(self,customer_id,helper_id):
        return self.model.objects.filter(
            customer_id = customer_id ,
            helper_id = helper_id,
            is_used = False,
        ).exists()











    # def latest(self,customer,store):
    #     if self.model.objects.filter(customer = customer,store = store,)\
    #             .exclude(share=None).exists() is True:
    #         return  self.model.objects.filter(customer = customer,store = store,)\
    #             .exclude(share=None)[0]
    #     else:
    #         return False
    #
    # '''
    #     @method 用户可用点数
    #     @summary 查询店铺有效期内的点数，有效期范围外的不计入
    #     @param
    #         store_uuid    店铺uuid
    #         customer_uuid 顾客uuid
    #     @return 有效总数
    # '''
    # def count_valid(self,store_uuid,customer_uuid):
    #     db_store = DBStore()
    #     store = db_store.get(uuid = store_uuid)
    #     return self.model.objects.filter(
    #         store = store,
    #         customer__uuid = customer_uuid,
    #         is_used = False,
    #         is_delete = False,
    #         create_time__gt = store.start_time,
    #         create_time__lt = store.end_time,
    #     ).count()




if __name__ == '__main__':
    import django
    django.setup()
    s = DBScore()
    share = Share.objects.get(id=18)
    customer = Customer.objects.get(id=1)
    score = Score.objects.filter(seller__uuid = '6a6c8366-7606-11e9-9df9-e95aa2c51b5d')[0:10]
    print( score)
    # print (s.filter(seller__uuid = '6a6c8366-7606-11e9-9df9-e95aa2c51b5d'))
    # print (s.latest(customer,share.store))
    # query = { 'store_': 1}
    # l =  s.get_list(**query )
    # print (l)