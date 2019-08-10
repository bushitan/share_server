#coding:utf-8

from photo.db.db_article import *
from photo.db.db_gallery import *
from photo.db.db_prize import *
from photo.db.db_score import *
from photo.db.db_store import *
from photo.db.db_tag import *
from photo.db.db_user import *
from photo.db.db_base_image import *
from photo.db.db_like import *

class DBUtils():
    # article = 1
    def __init__(self):
        # pass
        self.article = DBArticle()
        self.gallery = DBGallery()
        self.prize = DBPrize()
        self.score = DBScore()
        self.store = DBStore()
        self.tag = DBTag()
        self.user = DBUser()
        self.base_image = DBBaseImage()
        self.like = DBLike()
db = DBUtils()

if __name__ == "__main__":
    print (db.article.all())
    print (db.article.is_exists(id = 2 ))

