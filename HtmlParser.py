# coding=utf-8
import re
from bs4 import BeautifulSoup
class HtmlParser(object):
    def __getNewDatas__(self,soup):
        d={}
        # https://www.anjuke.com/tianjin/cm
        price=soup.find("p",class_='av-price').find('em',class_='num').text

        d[u'price'] = price+u"元/平米"
        infos = soup.find("ul",class_='basic-parms').find_all("li")
        for info in infos:
            L = info.contents
            k = unicode(L[0])
            v = L[1].text
            d[k]=v
        return d
       
    '''
        page_url:当前正在解析的网页
        html_cont:正在解析的网页上的内容
    '''    
    def parse(self,html_cont):
        if html_cont is None:
            return
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        datas = self.__getNewDatas__(soup)
        return datas
