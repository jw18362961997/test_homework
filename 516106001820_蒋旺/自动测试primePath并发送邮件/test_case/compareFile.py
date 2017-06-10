import hashlib  
import difflib
import sys

def getHash(f):  
    line=f.readline()  
    hash=hashlib.md5()  
    line = line.strip()
    while(line.strip()):  
        hash.update(line)  
        line=f.readline()  
    return hash.hexdigest()  
def IsHashEqual(f1,f2):  
    str1=getHash(f1)  
    str2=getHash(f2)  
    return str1==str2  
  

def doBatchTest():
    basePath1 = "C:\\Users\\Gin\\Desktop\\功能自动化测试框架\\primePath"
    basePath2 = "C:\\Users\\Gin\\Desktop\\功能自动化测试框架\\代码题\\hshanswer"
    for i in range(16):
        f1 = open(basePath1 + "\\answer" + str(i) + ".txt","rb")
        f2 = open(basePath2 + "\\answer" + str(i) + ".txt","rb")
        #a = open('a.txt', 'U').readlines()
        #  b = open('b.txt', 'U').readlines()
        #diff = difflib.ndiff(f1, f2)
        #print( f1 == f2)
        #sys.stdout.writelines(diff)
        print("第" +str(i) +"个：" ,IsHashEqual(f1,f2)  )

    print("结束")

if __name__ == '__main__':
    doBatchTest()