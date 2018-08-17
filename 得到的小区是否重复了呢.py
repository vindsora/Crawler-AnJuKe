# coding=utf-8
from lib import JsonUtils
'''
    重复了
    比如 
    瑞湾国际汇馆
熙汇广场
京港国际城
荣泽大厦
瑞海金岸
仁恒海河广场
首创禧悦汇
联发第五街
悦公馆
绿岛新城
浙商大厦
贻成峰景
馨苑小区
锦尚豪庭
'''
ju = JsonUtils.JsonUtils()
xqs = ju.readFile(u'f:\\ajk\\小区\\天津_所有小区.json')
S = set([])
for xq in xqs:
    xqName = xq[u'xqName']
    if(xqName in S):
        print xqName
    S.add(xq[u'xqName'])
print len(S),len(citys)