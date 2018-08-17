# coding=utf-8
from lib import HtmlDownloader
from lib import HtmlOutputer
from bs4 import BeautifulSoup
from lib import JsonUtils
import re
ju = JsonUtils.JsonUtils()
hd = HtmlDownloader.HtmlDownloader()
ho = HtmlOutputer.HtmlOutputer()
#url = u"https://www.anjuke.com/tianjin/cm/"
citys = ju.readFile(u'F:\\ajk\\城市列表及其对应的url.json')
L=[]
for city in citys:
    cityUrl = city[u'cityUrl']
    cityName = city[u'cityName']
    print cityName,cityUrl
    html_cont = hd.download4(cityUrl)
    while html_cont is None:
        print "retrying..."+cityUrl
        html_cont = hd.download(cityUrl)
    html_cont = unicode(html_cont,'utf-8')
    soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
    pages = soup.find(text=re.compile(u'快速页码')).parent
    print len(pages.find_all('a'))
    pageNum = len(pages.find_all('a'))
    pages = unicode(str((pageNum-1)*1000))+u"-"+unicode(str(pageNum*1000))
    print pages
    L.append({u"cityName":cityName,u"cityUrl":cityUrl,u"小区数":pages})
ho.outputList2html(u"F:\\ajk\\城市名_URL_小区数.html",L)
ju.writeJson2File(u"F:\\ajk\\城市名_URL_小区数.json",L)
