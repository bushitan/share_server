#coding:utf-8
from photo.db.db import DB
from photo.models import *


class DBArticle(DB):
    def __init__(self):
        super().__init__(Article)

    # 基础的查询数据
    def _pack_dict(self,object):
        _base = super()._pack_dict(object)



        # if object.tag_id == 2:
        #     cover =  "%s?imageView2/2/w/750" % ( object.cover )
        # else:
        #     cover = object.cover
        cover = object.cover
        cover = cover.replace("https://www.51zfgx.com", "http://img.12xiong.top")
        _new = {
            # "poi_id":object.poi_id,
            # "type":object.type,

            "tag_id":object.tag_id ,
            
            "cover":cover,
            "title":object.title,
            "summary":object.summary,
            "description":object.description,
            "content":object.content,
            "url":object.url,

            "author_logo":object.author_logo,
            "author_name":object.author_name,

            "like_count":object.like_count,


            # "url":object.url,
            # "qr":object.qr.url if object.qr is not None else "" ,
            #
            #
            # "author_nick_name":object.author.nick_name if object.author is not None else "" ,
            # "author_avatar_url":object.author.avatar_url if object.author is not None else "" ,
        }
        return dict(_base,**_new)


      # 获取poi的详情，获取相关文章
    def get_list_by_show(self):
        _m = self.model.objects.filter(is_show = True)
        return self._pack_list( self._pack_dict,_m)

    def addLike(self,article_id):
        _m = self.model.objects.get(id = article_id)
        _m.like_count = _m.like_count + 1
        _m.save()



    # 获取poi的详情，获取相关文章
    def get_list_by_poi(self,poi_id):
        _m = self.model.objects.filter(poi_id=poi_id, is_show = True)
        return self._pack_list( self._pack_dict,_m)




if __name__ == '__main__':
    import django
    django.setup()
    s = DBArticle()

    print( s.all() )
    # l = s.get_list()
    # print (l)