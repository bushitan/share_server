#coding:utf-8
from django.conf.urls import url
from .views import  *

urlpatterns = [


    # url(r'^system/login/',SystemLogin.as_view()), #登陆获取uuid
    url(r'^system/login/',SystemLogin.as_view()), #登陆获取uuid
    url(r'^system/set/user_info/',SystemAddUserInfo.as_view()), #增加客户信息


    url(r'^article/get/rule/',ArticleGetRule.as_view()), #增加客户信息

    url(r'^article/get/list/',ArticleGetList.as_view()), #获取标签，文章列表
    url(r'^article/get/detail/',ArticleGetDetail.as_view()), #获取文章详情


    url(r'^customer/get/user_info/',CustomerGetInfo.as_view()), #获取当天的分数和礼物领取情况
    url(r'^customer/get/photo_list/',CustomerGetPhotoList.as_view()), #获取获取照片墙列表
    url(r'^customer/get/token/',CustomerGetToken.as_view()), #获取七牛云的token
    url(r'^customer/add/photo/',CustomerAddPhoto.as_view()), #增加照片
    url(r'^customer/get/qr/',CustomerGetQR.as_view()), #获取分享二维码
    url(r'^customer/get/like_list/',CustomerGetLikeList.as_view()), #点赞
    url(r'^customer/add/like/',CustomerAddLike.as_view()), #点赞
    url(r'^customer/add/help/',CustomerAddHelp.as_view()), #朋友助力获取积分

    url(r'^seller/add/check/',SellerAddCheck.as_view()), #店家核销
    url(r'^seller/get/check_list/',SellerGetCheckList.as_view()), #店家获取核销列表







    # url(r'^scan/info/',SellerScanPrize.as_view()),

 # url(r'^store/invite/seller/',SellerInvite.as_view()),
 #    url(r'^store/quit/seller/',SellerQuit.as_view()),
    # url(r'^store/apply/seller/',SellerApply.as_view()), # 暂无
    # url(r'^store/dissolve/seller/',Index55.as_view()),
]
