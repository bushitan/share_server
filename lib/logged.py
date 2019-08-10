#coding:utf-8

from django.http import HttpResponse
import json
from photo.message.message_utils import message
import json
import logging
logger = logging.getLogger("django") # 为loggers中定义的名称

# TODO 做统计的
def logged(func):
    def wrapper(self,request,*args, **kwargs):
        try:
            _dict = func(self,request,*args, **kwargs)
            if _dict.__contains__("message") is False:
                _dict["message"] = message.sys_success()
            return HttpResponse( json.dumps( _dict ),content_type="application/json" )
        except Exception as e:
            logger.error(self.__class__.__name__ +" ---- " + str(e)) #打印错误日志
            _dict = {
                'message':message.sys_error() ,
                'class_name': self.__class__.__name__,
                'error':  str(e)
            }
            return HttpResponse( json.dumps( _dict ),content_type="application/json" )
    return wrapper
