# coding=utf-8
import HtmlDownloader
import IOUtils
import JsonUtils
import HtmlOutputer
import re
from bs4 import BeautifulSoup
class HtmlParser(object):
    def __getNewDatas__(self,soup):
        new_datas = []
        # https://www.anjuke.com/tianjin/cm
        nodes = soup.find_all("a",href=re.compile(r"https://www.anjuke.com/tianjin/cm\d+"))
        for node in nodes[0:20:1]:
            name = node.text
            new_url = node['href']
            new_datas.append({u"小区名称":name,u"网站":new_url})
        return new_datas
       
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

ho = HtmlOutputer.HtmlOutputer()
hd = HtmlDownloader.HtmlDownloader()
url = 'https://www.anjuke.com/tianjin/cm/'
res = hd.download4(url)
res = unicode(res,'utf-8')
hp =HtmlParser()
datas = hp.parse(res)
print len(datas)
for data in datas:
    print data[u'小区名称'],data[u'网站']
io = IOUtils.IOUtils()
io.writeListOrDict2JsonFile("F:\\ajk\\info.json",datas)
ho.outputList2html("F:\\ajk\\info.html",datas)