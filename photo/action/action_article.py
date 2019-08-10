#coding:utf-8

from django.db import transaction
from photo.db.db_utils import db
from lib.util import *
import time
import datetime
'''
    @method CMS内容
    @fun
    	1、列表、标签欻性能
    	2、文章内容查询
'''
class ActionArticle():
    def __init__(self):
        pass

    '''
        @method 文章列表
    '''
    def get_article_list(self):
        return db.article.get_list_by_show()

    '''
        @method 标签列表
    '''
    def get_tag_list(self):
        return db.tag.get_list()

    '''
        @method 文章内容
    '''
    def get_detail_by_id(self,article_id):
        return db.article.get_dict( id = article_id )








