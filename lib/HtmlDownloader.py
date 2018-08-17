# coding=utf-8
import urllib2,cookielib
import sys
class HtmlDownloader(object):
    '''
        下载一个网页，返回该网页上的内容。如果抛出异常，则返回None
    '''
    def download(self,url):
        if url is None:
            return None
        try:
            response = urllib2.urlopen(url)
        except :
            info=sys.exc_info()  
            print info[0],":",info[1]
            return None
        else:
            if response.getcode() != 200:
                return None
            return response.read()
        finally:
            pass
    def download2(self,url):
        request = urllib2.Request(url)
        request.add_data('a','1')
        request.add_header('User-Agent','Mozilla/5.0')
        response = urllib2.urlopen(request)
        
    def download3(self,url):
        opener = urllib2.build_opener(handler)
        urllib2.install_opener(opener)
        
        cj = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        urllib2.install_opener(opener)
        response = urllib2.urlopen("http://www.baidu.com")
    
    def download4(self,url):
        if url is None:
            return None
        try:
            httpsHandler = urllib2.HTTPSHandler()
            opener = urllib2.build_opener(httpsHandler)
            urllib2.install_opener(opener)
            
            request = urllib2.Request(url)
            request.add_header('User-Agent','Mozilla/5.0')
            response = urllib2.urlopen(request)
        except :
            info=sys.exc_info()  
            print info[0],":",info[1]
            return None
        else:
            if response.getcode() != 200:
                return None
            return response.read()
        finally:
            pass
            
import codecs
import json
if __name__ == "__main__":
    hd = HtmlDownloader()
    url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv44296&productId=2155914&score=3&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1'
    print hd.download4(url)