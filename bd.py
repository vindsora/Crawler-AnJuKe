# coding=utf-8
import HtmlDownloader
import urllib2
from lib import JsonUtils
'''
查询地理位置
    place:要查询的地理位置
    city:所在的城市
'''
def getPos(place,city):
    ak = u'BjZFyCBFktfZmdj7SVP98fEFx78KzFn4'
    
    d={}
    place=urllib2.quote(place)
    city=urllib2.quote(city)
    hd = HtmlDownloader.HtmlDownloader()
    ju =  JsonUtils.JsonUtils()
    url =u'http://api.map.baidu.com/geocoder/v2/?address=%s&output=json&ak=%s&city=%s' %(place,ak,city)
    #print url
    res = hd.download(url)
    res = unicode(res,'utf-8')
    data = ju.readStr(res)

    status = data[u'status']
    if status==0:
        lng = data[u'result'][u'location'][u'lng']
        lat = data[u'result'][u'location'][u'lat']
        d[u"精度"]=unicode(str(lng),"utf-8")
        d[u"纬度"]=unicode(str(lat),'utf-8')
        return d
    else:
        return None
def getPOI(key,radius,lat,lng):
    ak = u'BjZFyCBFktfZmdj7SVP98fEFx78KzFn4'
    key = urllib2.quote(key)
    hd = HtmlDownloader.HtmlDownloader()
    ju =  JsonUtils.JsonUtils()
    url = 'http://api.map.baidu.com/place/v2/search?query=%s&location=%s,%s&radius=%s&output=json&ak=%s&page_size=20' %(key,lat,lng,radius,ak)
    #print url
    res = hd.download(url)
    res = unicode(res,'utf-8')
    data = ju.readStr(res)
    status = data[u'status']
    total = u'0'
    L =[]   
    if status==0:
        total = data[u'total']
        total,unicode(str(total),'utf-8')
        ress = data[u'results']
        for res in ress:
            L.append(res['name'])
    else:
        pass
    return total,len(ress),L  

if __name__=='__main__':
    print getPos('恒大绿洲南区','太原')
    print getPos('山西大学','太原')
    print getPos('银杏苑','大理')
    d = getPos('山西大学','太原')
    d = getPos('恒大绿洲南区','太原')
    r = 500
    total,num,L = getPOI('大学',r,d[u"纬度"],d[u"精度"])
    print total
    total,num,L = getPOI('中学',r,d[u"纬度"],d[u"精度"])
    print total
    total,num,L = getPOI('幼儿园',r,d[u"纬度"],d[u"精度"])
    print total
    total,num,L = getPOI('菜市场',r,d[u"纬度"],d[u"精度"])
    print total
    total,num,L = getPOI('医院',r,d[u"纬度"],d[u"精度"])
    print total
