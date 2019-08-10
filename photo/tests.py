#coding:utf-8
# from django.urls import resolve, reverse
from django.test import TestCase
from share_server.settings import ENV_URL
import json

APP = "photo/"
class Demo(TestCase):
    fixtures = ['mysql.json']

    def setUp(self):
        # print('setUp')
        self.name = 'Django'

    # def test_heelow_test_case(self):
    #     print('test_heelow')


    # def test_hello_test_case(self):
    #     url = '/' + ENV_URL + 'photo/base/login/'
    #     response = self.client.post(url)
    #     self.assertEqual(response.status_code, 200)  # 期望的Http相应码为200
    #
    #     data = json.loads(str(response.content,'utf-8'))
    #     print ('test_hello_test_case',data)
    #     self.assertEqual(data['message']['code'], '200001')  # 期望的msg返回结果为'Hello , I am a test Case'

    '''
        @method 系统更新用户信息
    '''
    def test_sys_set_user_info(self):
        url = '/' + ENV_URL + APP + 'system/set/user_info/'
        data = {
            "uuid":'1cff3e06-adf7-11e9-b8ce-e95aa2c51b5d', #丰兄
            'nickName':'this.丰兄 (¦(¦',
            'avatarUrl':'21321',
            'gender':'',
            'city':'',
            'province':'',
            'country':'',
        }
        response = self.client.post(url,data = data)
        self.assertEqual(response.status_code, 200)  # 期望的Http相应码为200
        data = json.loads(str(response.content,'utf-8'))
        print ('test_sys_set_user_info',data)


    '''
        @method 查询文章详情
    '''
    def test_article_get_list(self):
        url = '/' + ENV_URL + APP + 'article/get/list/'
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)  # 期望的Http相应码为200
        data = json.loads(str(response.content,'utf-8'))
        print ('test_article_get_detail',data)



    '''
        @method 查询文章详情
    '''
    def test_article_get_detail(self):
        url = '/' + ENV_URL + APP + 'article/get/detail/'
        data = {"article_id": 1}
        response = self.client.post(url,data = data)
        self.assertEqual(response.status_code, 200)  # 期望的Http相应码为200
        data = json.loads(str(response.content,'utf-8'))
        print ('test_article_get_detail',data)


    '''        customer用户模块           '''
    def test_customer_get_info(self):
        url = '/' + ENV_URL + APP + 'customer/get/user_info/'
        data = {
            "uuid":'1cff3e06-adf7-11e9-b8ce-e95aa2c51b5d', #丰兄
            "uuid":'1cff3e06-adf7-11e9-b8ce-', #丰兄
        }
        response = self.client.post(url,data = data)
        self.assertEqual(response.status_code, 200)  # 期望的Http相应码为200
        data = json.loads(str(response.content,'utf-8'))
        print ('test_customer_get_info',data)


    def test_customer_get_photo_list(self):
        url = '/' + ENV_URL + APP + 'customer/get/photo_list/'
        data = {
            "uuid":'1cff3e06-adf7-11e9-b8ce-e95aa2c51b5d', #丰兄
        }
        response = self.client.post(url,data = data)
        self.assertEqual(response.status_code, 200)  # 期望的Http相应码为200
        data = json.loads(str(response.content,'utf-8'))
        print ('test_customer_get_photo_list',data)

    '''骑牛token'''
    def test_customer_get_token(self):
        url = '/' + ENV_URL + APP + 'customer/get/token/'
        data = {
            "uuid":'1cff3e06-adf7-11e9-b8ce-e95aa2c51b5d', #丰兄
        }
        response = self.client.post(url,data = data)
        self.assertEqual(response.status_code, 200)  # 期望的Http相应码为200
        data = json.loads(str(response.content,'utf-8'))
        print ('test_customer_get_photo_list',data)


    '''骑牛token'''
    def test_customer_add_photo(self):
        url = '/' + ENV_URL + APP + 'customer/add/photo/'
        data = {
            "uuid":'1cff3e06-adf7-11e9-b8ce-e95aa2c51b5d', #丰兄
            'image_url':"1232"
        }
        response = self.client.post(url,data = data)
        self.assertEqual(response.status_code, 200)  # 期望的Http相应码为200
        data = json.loads(str(response.content,'utf-8'))
        print ('test_customer_add_photo',data)


    '''点赞'''
    def test_customer_get_like_list(self):
        url = '/' + ENV_URL + APP + 'customer/get/like_list/'
        data = {
            "uuid":'1cff3e06-adf7-11e9-b8ce-e95aa2c51b5d', #丰兄
        }
        response = self.client.post(url,data = data)
        self.assertEqual(response.status_code, 200)  # 期望的Http相应码为200
        data = json.loads(str(response.content,'utf-8'))
        print ('test_customer_get_like_list',data)


    '''点赞'''
    def test_customer_add_like(self):
        url = '/' + ENV_URL + APP + 'customer/add/like/'
        data = {
            "uuid":'1cff3e06-adf7-11e9-b8ce-e95aa2c51b5d', #丰兄
            'article_id':1
        }
        response = self.client.post(url,data = data)
        self.assertEqual(response.status_code, 200)  # 期望的Http相应码为200
        data = json.loads(str(response.content,'utf-8'))
        print ('test_customer_add_photo',data)



    '''点赞'''
    def test_customer_add_like(self):
        url = '/' + ENV_URL + APP + 'customer/add/help/'
        data = {
            "uuid":'1cff3e06-adf7-11e9-b8ce-e95aa2c51b5d', #丰兄
            "customer_id":'1', #丰兄
        }
        response = self.client.post(url,data = data)
        self.assertEqual(response.status_code, 200)  # 期望的Http相应码为200
        data = json.loads(str(response.content,'utf-8'))
        print ('test_customer_add_like',data)




    '''店家核销'''
    def test_seller_add_check(self):
        url = '/' + ENV_URL + APP + 'seller/add/check/'
        data = {
            "uuid":'1cff3e06-adf7-11e9-b8ce-e95aa2c51b5d', #丰兄
            'customer_uuid':'1cff3e06-adf7-11e9-b8ce-e95aa2c51b5d'
        }
        response = self.client.post(url,data = data)
        self.assertEqual(response.status_code, 200)  # 期望的Http相应码为200
        data = json.loads(str(response.content,'utf-8'))
        print ('test_seller_add_check',data)


    '''店家获取核销列表'''
    def test_seller_get_check_list(self):
        url = '/' + ENV_URL + APP + 'seller/get/check_list/'
        data = {
            "uuid":'1cff3e06-adf7-11e9-b8ce-e95aa2c51b5d', #丰兄
            "page_num":0,
            "range":10
        }
        response = self.client.post(url,data = data)
        self.assertEqual(response.status_code, 200)  # 期望的Http相应码为200
        data = json.loads(str(response.content,'utf-8'))
        print ('test_seller_get_check_list',data)
    # CustomerGetInfo


    # def tearDown(self):
        # print('tearDown')
