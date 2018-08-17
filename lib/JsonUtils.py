# coding=utf-8
import json
import codecs
import sys
class JsonUtils(object):
    def readFile(self,filePath):
        fin = codecs.open(filePath,'r','utf-8')
        try:
            d = json.load(fin)
        except:
            info=sys.exc_info()  
            print info[0],":",info[1]
            return None 
        else:
            return d
        finally:
            fin.close()
    
    def readStr(self,str):
        try:    
            res = json.loads(str)
        except:
            info=sys.exc_info()  
            print info[0],":",info[1]
            return None
        else:
            return res
    
    def writeJson2Str(self,j):
        return json.dumps(j)
        
    def writeJson2File(self,filePath,datas):
        str = self.writeJson2Str(datas)
        fin = codecs.open(filePath,'w','utf-8')
        res = fin.write(str)
        fin.close()
 
    def formatJson(self,str):
        start= str.find("{")
        end= str.rfind("}")
        return str[start:end+1:1]

if __name__ == "__main__":        
    ju = JsonUtils()
    str="<!--KG_TAG_RES_START-->{dat{<>{}{}}{}a}<!--KG_TAG_RES_END-->"
    print ju.formatJson(str)
    print ju.readFile("F:\\listlist.txt")
    datas = [{u"姓名":u"张三",u"age":12},{u"姓名":u"张三",u"age":12},{u"姓名":u"张三",u"age":12}]
    print ju.writeJson2File(datas,"F:\\dda.json")
