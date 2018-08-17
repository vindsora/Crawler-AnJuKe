# coding=utf-8
import IOUtils
import HtmlDownloader
import HtmlParser
import HtmlOutputer
import bd

L=[]
hd = HtmlDownloader.HtmlDownloader()
hp = HtmlParser.HtmlParser()
io =IOUtils.IOUtils()
ho = HtmlOutputer.HtmlOutputer()
datas = io.getListOrDictFromJsonFile("F:\\ajk\\info.json")
print len(datas)
L_res=[]
for data in datas:
    name = data[u'小区名称']
    print name
    #下面这一步是为了url编码
    name = name.encode('utf-8') 
    url = data[u'网站']

    d = bd.getPos(name)
    if d is None:
        data[u'精度']=u"未找到"
        data[u'纬度']=u"未找到"
        data[u'附件500米幼儿园']=u"未找到"
        data[u'附近3000米幼儿园']=u"未找到"
        data[u'附近500米医院']=u"未找到"
        data[u'附近3000米医院']=u"未找到"
        data[u'附近500米商场']=u"未找到"
        data[u'附近3000米商场']=u"未找到"
    else:
        lng = d[u'精度']
        lat = d[u'纬度']
        total1,num,L = bd.getPOI("幼儿园",500,lat,lng)
        total2,num,L = bd.getPOI("幼儿园",3000,lat,lng)
        total3,num,L = bd.getPOI("医院",500,lat,lng)
        total4,num,L = bd.getPOI("医院",3000,lat,lng)
        total5,num,L = bd.getPOI("商场",500,lat,lng)
        total6,num,L = bd.getPOI("商场",3000,lat,lng)
        data[u'精度']=lng
        data[u'纬度']=lat
        data[u'附近500米幼儿园']=total1
        data[u'附近3000米幼儿园']=total2
        data[u'附近500米医院']=total3
        data[u'附近3000米医院']=total4
        data[u'附近500米商场']=total5
        data[u'附近3000米商场']=total6
        L_res.append(data)
keys=[u"小区名称",u"精度",u"纬度",u"附近500米幼儿园",u"附近3000米幼儿园",u"附近500米医院",u"附近3000米医院",u"附近500米商场",u"附近3000米商场"]
ho.outputList2html2('f:\\sss.html',L_res,keys)