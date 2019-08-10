#coding:utf-8
from share_server.settings import *
import qiniu
import time
# 七牛配置 -- 表情袋
qiniu_access_key = 'bK5xWj0a-TBIljlxHYOHuQib9HYF_9Ft-HtP8tEb'
qiniu_secret_key = '56lucORYc45sF5eDqNk63mLXsQ78n4RrubIrjtE0'
qiniu_bucket_name = 'clickz'

COFFEE_IMAGE_SPACE = 'coffee_image/upload'

SHARE_PHOTO_IMAGE_SPACE = 'qiniu/share_photo_image/fang_te'
class ImageUtils:
    def __init__(self):
        pass

    def share_token(self,user_id):
        dt = time.strftime("%Y_%m_%d_%H_%M_%S",time.localtime(int(time.time())))
        name = str(user_id) + "_" + dt
        key = '%s/%s.%s' %( SHARE_PHOTO_IMAGE_SPACE,name  ,"jpg")
        q = qiniu.Auth(qiniu_access_key, qiniu_secret_key)
        token = q.upload_token(qiniu_bucket_name, key)
        return key,token


    @staticmethod
    def rename(instance, filename):
        suffix = filename.split('.')[-1]
        key = '%s/%s.%s' %( COFFEE_IMAGE_SPACE,instance.short_uuid ,suffix)
        print ( os.path.isfile(MEDIA_ROOT+key))
        local_file = MEDIA_ROOT+key
        if os.path.isfile(local_file):
            os.remove(local_file)
        return key

    @staticmethod
    def put(key,local_file):
        q = qiniu.Auth(qiniu_access_key, qiniu_secret_key)
        token = q.upload_token(qiniu_bucket_name, key)
        ret, info = qiniu.put_file(token, key, local_file,check_crc=True)
        print (ret ,info)

image_utils = ImageUtils()

if __name__ == "__main__":
    #获取当前时间
    time_now = int(time.time())
    #转换成localtime
    time_local = time.localtime(time_now)
    #转换成新的时间格式(2016-05-09 18:59:20)

    # print (dt)
        # return '/upload/'.join([MEDIA_ROOT, instance.short_uuid, filename])