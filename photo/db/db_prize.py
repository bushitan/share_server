#coding:utf-8
from photo.db.db import DB
from photo.models import *


class DBPrize(DB):
    def __init__(self):
        super().__init__(Prize)

    # 基础的查询数据
    def _pack_dict(self,object):
        _base = super()._pack_dict(object)
        _new = {
            "prize_id":object.id,
            "seller_id":object.seller_id,
            "customer_id":object.customer_id,

		 	# "seller_avatar_url":object.seller.avatar_url if object.seller is not None else "" ,
            # "seller_nick_name":object.seller.nick_name if object.seller is not None else "" ,
            #
		 	# "customer_avatar_url":object.seller.avatar_url if object.seller is not None else "" ,
            # "customer_nick_name":object.seller.nick_name if object.seller is not None else "" ,
        }
        return dict(_base,**_new)


    '''
        @method 增加核销记录
    '''
    def get_check_list(self,seller_id,page_num,range):
        _m = self.model.objects.filter(id = seller_id)[page_num:range]
        return self._pack_list( self._pack_dict,_m)





if __name__ == '__main__':
    s = DBPrize()
    l = s.get_list()
    print (l)