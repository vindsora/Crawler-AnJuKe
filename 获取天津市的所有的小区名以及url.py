# coding=utf-8
from lib import HtmlDownloader
from lib import HtmlOutputer
from bs4 import BeautifulSoup
from lib import JsonUtils
import re
ju = JsonUtils.JsonUtils()
hd = HtmlDownloader.HtmlDownloader()
ho = HtmlOutputer.HtmlOutputer()
url = u"https://www.anjuke.com/tianjin/cm/p%s/"
cityName = u"天津"
dirName = u"F:\\ajk\\小区\\%s_所有小区" %(cityName)
L=[]
for page in range(1,34):
    myurl = url %(page)
    print myurl
    html_cont = hd.download4(myurl)
    while html_cont is None:
        print "retrying..."+myurl
        html_cont = hd.download(cityUrl)
    html_cont = unicode(html_cont,'utf-8')
    soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
    xqs = soup.find("div",id='container').find("div",id="content").find("ul",class_='P3')
    xqs = xqs.find_all('a',href=re.compile('https:.*cm\d+'))
    print len(xqs)
    for xq in xqs:
        xqUrl = xq[u'href']
        xqName = xq.text
        #print xqUrl,xqName
        L.append({u"xqName":xqName,u"xqUrl":xqUrl})
ho.outputList2html(dirName + u".html",L)
ju.writeJson2File(dirName + u".json",L)
