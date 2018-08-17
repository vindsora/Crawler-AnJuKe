# coding=utf-8
from lib import HtmlDownloader
from lib import HtmlOutputer
from bs4 import BeautifulSoup
from lib import JsonUtils
import re
ju = JsonUtils.JsonUtils()
hd = HtmlDownloader.HtmlDownloader()
ho = HtmlOutputer.HtmlOutputer()
url = u"https://www.anjuke.com/tianjin/cm/"

html_cont = hd.download4(url)
while html_cont is None:
    print "retrying..."+url
    html_cont = hd.download(url)
html_cont = unicode(html_cont,'utf-8')
soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
qgxqdq = soup.find(text=u'全国小区大全')
tag_div =qgxqdq.parent.parent.parent
qgxqdq = tag_div.find_all('ul')[1]
#qgxqdq = .next_sibling

citys = qgxqdq.find_all('a',href=re.compile('https:.*/cm/'))
print len(citys)
L = []
for city in citys:
    cityName = city.text
    cityUrl = city[u'href']
    print cityName,cityUrl
    L.append({u"cityName":cityName,u"cityUrl":cityUrl})
ho.outputList2html(u"F:\\ajk\\城市列表及其对应的url.html",L)
ju.writeJson2File(u"F:\\ajk\\城市列表及其对应的url.json",L)
