#coding:utf-8
from photo.db.db import DB
from photo.models import *
import base64

class DBUser(DB):
    def __init__(self):
        super().__init__(User)

    # 基础的查询数据
    def _pack_dict(self,object):
        _base = super()._pack_dict(object)
        _new = {
            "user_id":object.id,
            "is_seller":object.is_seller,

            "name":object.name,
            "create_time":object.create_time.strftime("%Y-%m-%d"),
            "uuid":object.uuid,
            "nick_name":object.nick_name,
            "avatar_url":object.avatar_url,
            "gender":object.gender,
            "city":object.city,
            "province":object.province,
            "country":object.country,

            "name":object.name,
            "phone":object.phone,

            "wx_openid":object.wx_openid,
            "wx_session":object.wx_session,
            "wx_unionid":object.wx_unionid,

        }
        return dict(_base,**_new)

    def update_info(self,user_id,*args,**kwargs):
        user = self.model.objects.filter(id = user_id).update(
            name = kwargs['name'],
            phone = kwargs['phone'],
			nick_name_base64 =   str(base64.b64encode( kwargs['nick_name'].encode('utf-8')),'utf-8'),
			avatar_url =kwargs['avatar_url'],
			gender = kwargs['gender'],
			city = kwargs['city'],
			province = kwargs['province'],
			country = kwargs['country']
		)



		# # nick_name = u'this.丰胸' + nick_name
		# count = db.user.update_info(
		# 	user_id,
		# )
        #
		# 	update(
		# 	user,
		# 	# nick_name = request.POST.get('nickName',''), # 不再用nick_name 做存储
		# 	nick_name_base64 =   str(base64.b64encode( nick_name.encode('utf-8')),'utf-8'),
		# 	avatar_url =avatar_url,
		# 	gender = gender,
		# 	city = city,
		# 	province = province,
		# 	country = country
		# )

if __name__  == '__main__':
    pass
    # a= DBCustomer()
    # a.get(uuid = '67e3f912-63d4-11e9-9b5d-b83312f00bac')
