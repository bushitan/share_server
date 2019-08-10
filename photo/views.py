#coding:utf-8

import base64

from django.views.generic import ListView

from lib.logged import logged
from photo.detection.detection_utils import detection
from photo.message.message_utils import message
from photo.action.action_utils import action
from lib.util import *



class ErrorTest(ListView):
    @logged
    @detection.user_exist
    def post(self, request, *args, **kwargs):

        nick_name = request.POST.get('nickName','')
        nick_name = base64.b64encode(nick_name.encode('utf-8'))
        print (nick_name)

        decode =  base64.b64decode(nick_name)
        print (decode)

        return {
            # 'message':message.sys_success() ,
            'data': '123'
        }
        # raise (u"shaidhsa 粗哦无敌")




'''
    @method 系统登陆
    @param
        code
        uuid
    @return
        user_info 用户信息
'''
class SystemLogin(ListView):
    @logged
    # @detection.user_exist
    def post(self, request, *args, **kwargs):
        code = request.POST.get('code','')
        uuid = request.POST.get('uuid','')
        user_info = action.system.check_session(code,uuid)
        return {
            'data': {
                "user_info":user_info
            }
        }


'''
    @method 更新用户信息
    @param
        uuid
        nickName
        avatarUrl
        gender
        city
        province
        country
'''
class SystemAddUserInfo(ListView):
    @logged
    @detection.user
    def post(self, request, *args, **kwargs):
        action.system.update_user_info(
            kwargs['user_id'],
            name = request.POST.get('name',''),
            phone = request.POST.get('phone',''),
            nick_name = request.POST.get('nickName',''),
            avatar_url = request.POST.get('avatarUrl',''),
            gender =request.POST.get('gender',''),
            city =request.POST.get('city',''),
            province = request.POST.get('province',''),
            country = request.POST.get('country','')
        )
        return {
            'data': {}
        }


##################文章API########################

'''
    @method 获取活动规则
'''
class ArticleGetRule(ListView):
    @logged
    def post(self, request, *args, **kwargs):
        rule = '''
  <section data-role="outer" label="Powered by 135editor.com" style="font-size:16px;">
    <section class="_135editor" data-tools="135编辑器" data-id="95104"></section>
    <section class="_135editor" data-tools="135编辑器" data-id="95104">
        <section class="_135editor">
            <section style="text-align: center;">
                <section>
                    <section class="135brush" data-brushtype="text" style="margin-bottom:-10px;font-size: 16px;letter-spacing: 1.5px;color: #d32a63;font-weight: bold; text-align: center;">
                        晒方特夜景赢取千元福利
                    </section>
                </section>
            </section>
        </section>
    </section>
    <section class="_135editor" data-role="paragraph" >
        <p>
            &nbsp; &nbsp;
        </p>
    </section>
    <section class="_135editor" data-tools="135编辑器" data-id="85398" data-color="#d32a63" data-custom="#d32a63">
        <section class="layout" style="margin: 0px auto; padding: 0px 5px; line-height: 10px; color: inherit; border: 2px solid #d32a63; box-sizing: border-box;">
            <section style="padding: 0px; font-size: 16px; color: inherit; height: 8px; margin: -8px 4% 0px; background-color: #fefefe; box-sizing: border-box;"></section>
            <section class="135brush" data-style="text-align:justify" style="padding: 0px; line-height: 2em; color: #3e3e3e; font-size: 14px; margin: 15px 10px; box-sizing: border-box;">
                <p style="text-align:justify;" align="justify">
                    <span style="color: #d32a63;"><strong style="caret-color: red;"><span style="caret-color: red;">1.</span></strong></span><strong style="caret-color: red;"><span style="caret-color: red;">&nbsp;</span></strong><span style="caret-color: red;">选择<strong>【我的照片】</strong>菜单，点击“<strong>【拍照】</strong>”，图标上传您在南宁方特拍摄的夜景作品，并添加联系方式登录提交，即视为投稿成功。</span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
                </p>
                <p>
                    &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
                </p>
                <p>
                    <strong><span style="color: #d32a63;">2. </span></strong>我们将根据作品质量从每天投稿作品中挑选符合参赛规则的进入<strong>【精选作品】</strong>，被选中<strong>【精选作品】</strong>的参赛者可将自己作品分享给好友，为您点赞助力赢取华为手机大奖！
                </p>
                <p>
                    &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
                </p>
            </section>
        </section>
    </section>
    <p>
        <br/>
    </p>
</section>
<section class="_135editor" data-role="paragraph">
    <p>
        <br/>
    </p>
</section>
        '''
        return {
            'data': {
                "rule":rule,
            }
        }
'''
    @method 获取文章列表、标签
    @param
    @return
        article_list 文章列表
        tag_list 标签列表
'''
class ArticleGetList(ListView):
    @logged
    def post(self, request, *args, **kwargs):
        return {
            'data': {
                "article_list":action.article.get_article_list(),
                "tag_list":action.article.get_tag_list(),
            }
        }

'''
    @method 获取文章详情
    @param
    @return
        cover_list 文章列表
        tag_list 标签列表
'''
class ArticleGetDetail(ListView):
    @logged
    @detection.article_exist
    def post(self, request, *args, **kwargs):
        article_id = request.POST.get('article_id','')
        return {
            'data': {
                "article_detail":action.article.get_detail_by_id(article_id),
            }
        }


##################用户API########################
'''
    @method 获取用户信息（积分）
    @param
        uuid
    @return
        user_info 用户信息
'''
class CustomerGetInfo(ListView):
    @logged
    @detection.user
    def post(self, request, *args, **kwargs):
        # user_id = request.POST.get('user_id','')
        user_id = kwargs['user_id']
        print ("1111111:",user_id)
        return {
            'data': {
                "count_score":action.user.get_count_score(user_id),
            }
        }

'''
    @method 获取用户照片列表
    @param
        uuid
    @return
        photo_list 照片列表
'''
class CustomerGetPhotoList(ListView):
    @logged
    @detection.user
    def post(self, request, *args, **kwargs):
        user_id = kwargs['user_id']
        return {
            'data': {
                "photo_list":action.user.get_photo_list(user_id),
            }
        }

'''
    @method 获取上传图片的token
    @param
        uuid
    @return
        token 七牛token
'''
class CustomerGetToken(ListView):
    @logged
    @detection.user
    def post(self, request, *args, **kwargs):
        user_id = kwargs['user_id']
        key , token = action.user.get_qiniu_token(user_id)
        return {
            'data': {
                "key":key,
                "token":token,
            }
        }

'''
    @method 上传图片成功
    @param
        uuid
        image_url
'''
class CustomerAddPhoto(ListView):
    @logged
    @detection.user
    def post(self, request, *args, **kwargs):
        user_id = kwargs['user_id']
        image_url = request.POST.get('image_url','')
        r = action.user.add_photo(user_id ,image_url)
        if r is True :
            m = message.user_add_success()
        else:
            m = message.user_add_full()
        return {
            'message': m
        }

'''
    @method 获取二维码
    @param
    @return
        qr 二维码数据
'''
class CustomerGetQR(ListView):
    @logged
    @detection.user
    def post(self, request, *args, **kwargs):
        user_id = kwargs['user_id']

        # TODO 获取qr的base64
        return {'data': {
            "qr_base64": action.system.get_qr_base64(user_id)
        }}



'''
    @method 获取点赞列表
    @param
        uuid
'''
class CustomerGetLikeList(ListView):
    @logged
    @detection.user
    def post(self, request, *args, **kwargs):
        user_id = kwargs['user_id']
        return {
            'data':{"like_list":action.user.get_like_list(user_id)}
        }



'''
    @method 用户点赞
    @param
        uuid
        article_id
'''
class CustomerAddLike(ListView):
    @logged
    @detection.user
    def post(self, request, *args, **kwargs):
        user_id = kwargs['user_id']
        article_id = request.POST.get('article_id','')
        if action.user.add_like(user_id,article_id) is True:
            return {'message': message.sys_success()}
        else:
            return {'message': message.user_customer_is_like()}

'''
    @method 朋友助力获取积分
    @param
        uuid
        article_id
'''
class CustomerAddHelp(ListView):
    @logged
    @detection.user
    def post(self, request, *args, **kwargs):
        helper_id = kwargs['user_id'] #助力的好哟u
        customer_id = request.POST.get('customer_id','') #受帮助的用户id
        if action.user.add_score(customer_id,helper_id) is True:
            return {'message': message.user_customer_help_success()}
        else:
            return {'message': message.user_customer_is_help()}

######################商户核销# ##########################

'''
    @method 核销
    @param
        uuid
        customer_uuid
'''
class SellerAddCheck(ListView):
    @logged
    @detection.user
    @detection.scan
    def post(self, request, *args, **kwargs):
        seller_id = kwargs['user_id']
        customer_id =  kwargs['customer_id']
        # request.POST.get('customer_uuid','')
        if action.user.get_count_score(customer_id) < USER_CUSTOMER_PRIZE_LIMIT:
            return { 'message': message.user_customer_not_enough() }

        action.user.seller_check(seller_id,customer_id)
        return { "message":message.user_seller_success() }

'''
    @method 查询核销列表
    @param
        uuid
        article_id
'''
class SellerGetCheckList(ListView):
    @logged
    @detection.user
    def post(self, request, *args, **kwargs):
        seller_id = kwargs['user_id']
        page_num = int( request.POST.get('page_num',0))
        range = int(request.POST.get('range',10))
        prize_list = action.user.seller_get_check_prize_list(seller_id,page_num,range)
        return {
            'data': {
                "prize_list":prize_list
            }
        }
