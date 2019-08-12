#coding:utf-8
import math
from lib.util import *
DIALOG = "1"    #提示
HIDDEN = "2"    #隐藏
HACK   = "3"      #测试


SYS = "00"    #系统
USER = "01"     # 用户
ARTICLE = "02"     # 文章

class Message():
    # 00 系统
    SYS_SUCCESS = "%s%s001" %(HIDDEN,SYS)
    SYS_ERROR = "%s%s002" %(DIALOG,SYS)
    SYS_ERROR_NETWORK = "%s%s003" %(DIALOG,SYS)
    def sys_success(self):
        return {'code':self.SYS_SUCCESS,'title':u"请求成功" , 'content':u''}
    def sys_error(self):
        return {'code':self.SYS_ERROR,'title':u"系统超时" , 'content':u'请重新尝试'}
    def sys_error_network(self):
        return {'code':self.SYS_ERROR_NETWORK,'title':u"网络超时" , 'content':u'请重新尝试'}


    USER_CHECK_SUCCESS = "%s%s001" %(DIALOG,USER)  #扫码成功
    USER_NONE = "%s%s002" %(HIDDEN,USER)  #登陆失败
    USER_ADD_SUCCESS = "%s%s003" %(DIALOG,USER)  #更新失败
    USER_ADD_FULL = "%s%s004" %(DIALOG,USER)  #更新失败
    USER_CUSTOMER_NONE = "%s%s005" %(DIALOG,USER)  #扫码的顾客不存在
    USER_CUSTOMER_NOT_ENOUGH = "%s%s006" %(DIALOG,USER)  #扫码的顾客不存在
    USER_SELLER_SUCCESS = "%s%s007" %(DIALOG,USER)  #扫码的顾客不存在
    USER_CUSTOMER_IS_LIKE = "%s%s008" %(DIALOG,USER)  #扫码的顾客不存在
    USER_CUSTOMER_HELP_SUCCESS = "%s%s009" %(DIALOG,USER)  #扫码的顾客不存在
    USER_CUSTOMER_IS_HELP = "%s%s010" %(DIALOG,USER)  #扫码的顾客不存在
    def user_none(self):
        return {'code':self.USER_NONE,'title':u"用户不存在" , 'content':u''}
    def user_add_success(self):
        return {'code':self.USER_ADD_SUCCESS,'title':u"投稿成功" , 'content':u'请及时填写联系方式，若作品选中成为精选作品将会以电话形式通知您!'}
    def user_add_full(self):
        return {'code':self.USER_ADD_FULL,'title':u"用户上传满了" , 'content':u'仅能上传%s张照片' % (USER_MAX_UPLOAD_COUNT)}
    def user_check_success(self):
        return {'code':self.USER_CHECK_SUCCESS,'title':u"核销成功" , 'content':u''}
    def user_customer_none(self):
        return {'code':self.USER_CUSTOMER_NONE,'title':u"扫码的顾客不存在" , 'content':u''}
    def user_customer_not_enough(self):
        return {'code':self.USER_CUSTOMER_NOT_ENOUGH,'title':u"分享点数不足" , 'content':u''}
    def user_seller_success(self):
        return {'code':self.USER_SELLER_SUCCESS,'title':u"核销成功" , 'content':u''}
    def user_customer_is_like(self):
        return {'code':self.USER_CUSTOMER_IS_LIKE,'title':u"已经点赞" , 'content':u''}
    def user_customer_help_success(self):
        return {'code':self.USER_CUSTOMER_HELP_SUCCESS,'title':u"助力成功" , 'content':u'欢迎来到方特夜拍大赛'}
    def user_customer_is_help(self):
        return {'code':self.USER_CUSTOMER_IS_HELP,'title':u"已助力" , 'content':u''}




    ARTICLE_NONE = "%s%s002" %(DIALOG,ARTICLE)  #登陆失败
    def article_none(self):
        return {'code':self.ARTICLE_NONE,'title':u"文章不存在" , 'content':u''}

message = Message()