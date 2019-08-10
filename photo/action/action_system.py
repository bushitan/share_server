#coding:utf-8
from weixin import WeixinLogin
from photo.db.db_utils import db

# from photo.db.db_seller import *
import requests
import time
import json
import base64

import urllib
import urllib.request
from urllib import parse, request
'''
    @method 系统操作
    @fun
    	1、用户登录
    	2、获取系统token
    	3、二维码获取
'''
class ActionSys():
	def __init__(self,db_model,app_id,app_secret):
		self.db_user = db_model
		self.app_id = app_id
		self.app_secret = app_secret
		self.ACCESS_TOKEN = {'access_token':"",'expires_in':7200,'valid_unix':0}
		self.wxLogin = WeixinLogin(app_id, app_secret)

	# 根据js_code获取session
	def checkSession(self,code,uuid):
		# print code,user_id
		if uuid == "" or self.db_user.is_exists(uuid = uuid) is False:
			print (code , uuid)
			data = self.wxLogin.jscode2session(code) # self.getLogin(app_id,code)
			print (data)
			return self._checkUser(data) # 新用户存入
		return self.db_user.get_dict(uuid = uuid)

	# 获取不受限制的菊花吗
	def get_un_limit_qr(self,access_token ,data):

		file_name = data["scene"] + ".jpg" #按照sence，生成菊花码图片文件
		file_path = "C:\server\wxacodeunlimit/" + file_name
		self._post_qr(access_token ,data,file_path)
		return file_name

	# 获取外卖二维码
	def get_wm_qr(self,access_token ,data):
		file_name = data["scene"] + ".jpg" #按照sence，生成菊花码图片文件
		file_path = "C:/server/coffee_image/wm/" + file_name
		self._post_qr(access_token ,data,file_path)
		return file_name
	def _post_qr(self,access_token ,data,file_path):
		url = 'https://api.weixin.qq.com/wxa/getwxacodeunlimit?access_token=%s' % (access_token)
		headers = {'content-type': 'application/json'}
		r = requests.post(url,data=json.dumps(data), headers=headers )
		f=open(file_path,"wb")
		f.write(r.content)
		f.close()
		return True

	# 获取token
	def get_access_token(self):
		# print ('in token ', self.ACCESS_TOKEN)
		current_unix = time.time()
		if current_unix > self.ACCESS_TOKEN['valid_unix']:
			self._update_token()
		# print ('out token ',self.ACCESS_TOKEN)
		return self.ACCESS_TOKEN['access_token']


	# 更新touken
	def _update_token(self):
		expires_in = 7000
		current_unix = time.time()
		valid_unix = current_unix + expires_in
		_res = self._weixin_token()
		_res['valid_unix'] = valid_unix
		self.ACCESS_TOKEN = _res
		return  _res

	# 请求token
	def _weixin_token(self):
		url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' % (self.app_id , self.app_secret)
		r = requests.get(url)
		return json.loads( r.text)
		# print (int(t))
		# print(r.text)

	# 获取登陆信息
	# def getLogin(self,app_id,code):
	# 	if app_id == AII_ID_ZHAO_DD:
	# 		return login_zhaodd.jscode2session(code)
	# 	if app_id == AII_ID_COFFEE:
	# 		return login_coffee.jscode2session(code)
	# 	raise( 'APP_ID is null')

	# 检测用户是否存在
	def _checkUser(self,data):
		open_id = data['openid']
		session_key = data['session_key']
		# unionid = data['unionid']

		if self.db_user.is_exists(wx_openid = open_id) is True: #用户已存在，查询
			return self.db_user.get_dict(wx_openid = open_id)
		else: # 用户不存在，新增
			return self.db_user.add(
				wx_openid = open_id,
				wx_session = session_key,
				# wx_unionid = unionid,
			)





	##################新版本#####################

	'''
		@method 用户登陆，检测seesion
	'''
	def check_session(self,code,uuid):
		# print code,user_id
		if uuid == "" or db.user.is_exists(uuid = uuid) is False:
			data = self.wxLogin.jscode2session(code) # self.getLogin(app_id,code)
			open_id = data['openid']
			session_key = data['session_key']
			if db.user.is_exists(wx_openid = open_id) is True: #用户已存在，查询
				return db.user.get_dict(wx_openid = open_id)
			else: # 用户不存在，新增
				return db.user.add(
					wx_openid = open_id,
					wx_session = session_key,
					# wx_unionid = unionid,
				)
		return db.user.get_dict(uuid = uuid)






	'''
		@method 更新用户信息
		@param
			user_id 用户id
			**kwargs 详情
		@return
			count 更新成功的条数
	'''
	def update_user_info(self,user_id,*args,**kwargs):
		count =  db.user.update_info(user_id,*args,**kwargs)
		return count

	'''
		@method 根据用户id，生成短菊花码
		@param
			user_id 用户id
		@return
			image_base64 图片base64码
	'''
	def get_qr_base64(self,user_id):
		access_token = self.get_access_token()

		file_name = "wm_%s" % (user_id)
		file_path = "C:\server\wxacodeunlimit/" + file_name
		data = {
			"scene":file_name,
			"is_hyaline" :True,
		}
		url = 'https://api.weixin.qq.com/wxa/getwxacodeunlimit?access_token=%s' % (access_token)
		headers = {'content-type': 'application/json'}
		r = requests.post(url,data=json.dumps(data), headers=headers )

		f=open(file_path,"wb")
		f.write(r.content)
		f.close()
		return file_name

		# return 'data:image/png;base64,'+ base64.b64encode(r.content).decode('utf-8')



		# return r.content.decode('utf-8')
		# return r.text
		# return r.content

class ActionSystem(ActionSys):
	def __init__(self):
		super().__init__(db.user,'wxc3cb221202af930a','87b69ab0a8a29a1e67191ca2782d0e09')


if __name__  == '__main__':
	a= ActionSystem()

	print (a.get_qr_base64(1))


	# a.checkSession('011m3Wv42jb4IP0QRFy42cW0w42m3Wvu','')

	# str(b'123', encoding='utf-8')
	# a = bytes.decode(b'123')
	# print (a)
	# a.get_access_token()
	# data = {
     #        "scene":"sdfghjkl",
     #        "page":"pages/route/route",
     #    }
	# a.get_un_limit_qr("22_yZ9oeDbaM5z_G7-b7-0LPX1ahrcQAsoX4qntnBcAUYUU3yZqBHbTgqxNwY50xQ-yYYFb6K-Ob7FLwN_pKFAWZQ_rJuhOtk-2cjTJf3xju_js8jcbTX6YX1T9C_DvwJxmIaaAXEsfWO8ImVdiUEYhAAAAKE"
	# 				  ,data)