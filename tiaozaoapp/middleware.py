#自定义中间件类，（执行登录判断）
from  django.shortcuts import redirect
from  django.urls import  reverse
import re

class MIddleware:
    def __init__(self,get_response):
        self.get_response=get_response

        print('ShopMIddleware')

    def __call__(self,request):
        path=request.path
        print(path)

        #判断管理后台是否登录
        #定义后台不登录也可以访问的URL列表
        urllist=["/add/","/addB/","/insert/","/insertB/"]
        #判断当前url是否是/myadmin开头
        if path  in urllist:
            #判断是否登录
            if 'dolg' not in request.session:

                #重定向到登录页
                return  redirect(reverse('vLogin'))

        response = self.get_response(request)


        return response