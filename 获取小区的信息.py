# coding=utf-8
import IOUtils
import HtmlDownloader
import HtmlParser
import HtmlOutputer
L=[]
hd = HtmlDownloader.HtmlDownloader()
hp = HtmlParser.HtmlParser()
io =IOUtils.IOUtils()
ho = HtmlOutputer.HtmlOutputer()
datas = io.getListOrDictFromJsonFile("F:\\ajk\\info.json")
print len(datas)
for data in datas:
    name = data[u'小区名称']
    url = data[u'网站']
    print url
    res = hd.download4(url)
    while res is None:
        print "retrying ..."
        res = hd.download4(url)
    res = unicode(res,'utf-8')
    d = hp.parse(res)
    d[u'小区名']=name
    L.append(d)
io.writeList2TxtFile("F:\\ui.txt",L)
ho.outputList2html("F:\\ui.html",L)
io.writeListOrDict2JsonFile("F:\\ui.json",L)

    