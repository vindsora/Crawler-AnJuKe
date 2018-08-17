# coding=utf-8
import codecs
import sys
import json
import os
class IOUtils(object):

    def createNewFile(self,path):
        try:
            f = codecs.open(path,'w','utf-8')
        except:
            info=sys.exc_info()
            #print info[0],":",info[1]
            print u"create "+path+ u' failed'
            return False
        else:
            f.close()
            return True
        finally:
            pass
            
    def testPath(self,path):
        try:
            f = codecs.open(path,'w','utf-8')
        except:
            info=sys.exc_info()
            #print info[0],":",info[1]
            print u"create "+path+ u' failed'
            return False
        else:
            f.close()
            os.remove(path)
            return True
        finally:
            pass
    
    def write2File(self,path,str):
        try:
            f = codecs.open(path,'w','utf-8')
            f.write(str)
        except:
            info=sys.exc_info()
            print info[0],":",info[1]
        else:
            pass
        finally:
            if f:
                f.close()
            
    def append2File(self,path,str):
        try:
            f = codecs.open(path,'a','utf-8')
            f.write(str)
        except:
            info=sys.exc_info()  
            print info[0],":",info[1]
        else:
            pass
        finally:
            if f:
                f.close()
            
    def writeListOrDict2JsonFile(self,path,datas):
        res =json.dumps(datas)
        self.write2File(path,res)

    #将一个List写入文件 List的元素必须是dict
    def writeList2TxtFile(self,path,datas):
        try:
            f = codecs.open(path,'w','utf-8')
        except:
            info=sys.exc_info()  
            print info[0],":",info[1]
        else:
            i = 1
            for data in datas:
                rr = unicode(str(i),"utf-8")
                if isinstance(data,dict):
                    for key in data:
                        if isinstance(data[key],unicode):
                            rr = rr + u" " + data[key]
                        else:
                            rr = rr + u" " + unicode(str(data[key]),'utf-8')
                    rr = rr+ u'\r\n'
                elif isinstance(data,unicode):
                    rr = rr+u" "+data
                    rr = rr+u"\r\n"
                else:
                    rr = rr+u" "+unicode(str(data),"utf-8")
                    rr = rr + u"\r\n"
                f.write(rr)
                i = i+1
        finally:
            if f:
                f.close()
        
    def getListOrDictFromJsonFile(self,path):
        try:
            f = codecs.open(path,'r','utf-8')
        except:
            info=sys.exc_info()  
            print info[0],":",info[1]
            return None
        else:
            return json.load(f)
            f.close()
        finally:
            pass
            
if __name__ == "__main__":
    # 测试：写入数据到文件 从文件中读取数据
    io = IOUtils()
    io.writeListOrDict2JsonFile('f:\\listlist.txt',[{u"姓名":u"张中俊",u"年龄":12},{u"姓名":u"张s",u"年龄":100}])
    l = io.getListOrDictFromJsonFile('f:\\listlist.txt')
    print type(l)
    io.writeListOrDict2JsonFile('f:\\listlist.txt',{u"姓名":u"张中俊",u"年龄":12})
    l = io.getListOrDictFromJsonFile('f:\\listlist.txt')
    print type(l)
    io.writeList2TxtFile('f:\\listlist.txt',[{u"姓名":u"张中俊",u"年龄":u'12'},{u"姓名":u"张s",u"年龄":u'100'}])
    io.writeList2TxtFile('f:\\listlist2.txt',[{u"姓名":u"张中俊",u"age":u'12'},{u"姓名":u"张s",u"年龄":u'100'},{u"姓名":u"love",u"age":u'12'}])
    io.writeList2TxtFile('f:\\listlist3.txt',[{u"姓名":"张中俊",u"age":12},{"姓名":"张s",u"年龄":100},{u"姓名":u"love",u"age":u'12'}])
    print io.testPath(u"F:\\true.txt")
    print io.testPath(u"F:\\tr*ue.txt")