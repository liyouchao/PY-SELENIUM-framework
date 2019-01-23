"""
通过接口测试的client，对http接口添加httpclient，发送http请求
还可以封装tcpclient，用来通过tcp连接，测试socket接口等等
"""
import requests
from utils.log import logger

METHODS = ['GET','POST','HEAD','TRACE','PUT','DELETE','OPTIONS','CONNECT']

class UnSupporMethodException(Exception):
    #当传入的method的参数不是支持的类型是抛出异常
    pass

class HTTPclient(object):
    """
    http请求的client，初始化传入url，method等，可以添加header和cookies，但是没有auth，proxy。
    》》httpclient('http://www.baidu.com').send()
    《response 【200】》
    """
    def __init__(self,url,method='GET',headers=None,cookies=None):
        #headers:字典，如：headers{‘content_type’:'test/html'},cookies也是字典
        self.url = url
        self.session = requests.session()
        self.method = method.upper()  #upper()将小写转大写
        if self.method not in METHODS:
            raise UnSupporMethodException('不支持的method：{0},请检查传入参数！'.format(self.method))

        self.set_headers(headers)
        self.set_cookies(cookies)

    def set_headers(self,headers):
        if headers:
            self.session.headers.update(headers)

    def set_cookies(self,cookies):
        if cookies:
            self.session.cookies.update(cookies)

    def send(self,params=None,data=None,**kwargs):
        respomse = self.session.request(method=self.method,url=self.url,params=params,data=data,**kwargs)
        respomse.encoding = 'utf-8'
        logger.debug('{0} {1}'.format(self.method,self.url))
        logger.debug('请求成功：{0}\n{1}'.format(respomse,respomse.text))
        return respomse
