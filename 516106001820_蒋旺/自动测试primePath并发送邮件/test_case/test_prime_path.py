from selenium import webdriver
from primePath import doTest
from compareFile import IsHashEqual
import unittest, time
from HTMLTestRunner import HTMLTestRunner

class testPrimePath(unittest.TestCase):
    """primePath unit test测试"""

    def setUp(self):
        print("test start")

    def test_equal(self):
        i=1
        casePath = "C:\\Users\\Gin\\Desktop\\功能自动化测试框架\\代码题\\测试用例\\case"+str(i)+".txt"
        #basePath1 = "C:\\Users\\Gin\\Desktop\\功能自动化测试框架\\primePath")
        basePath2 = "C:\\Users\\Gin\\Desktop\\功能自动化测试框架\\代码题\\hshanswer"
        
        outFilePath = doTest(casePath, i)

        f1 = open(outFilePath,"rb")
        f2 = open(basePath2 + "\\answer" + str(i) + ".txt","rb")
        #print(outFilePath)
        equal = IsHashEqual(f1, f2)
       # equal=False
        self.assertEqual(equal, True)
    def tearDown(self):
        print("test end")

if __name__ == "__main__":
    
    testunit = unittest.TestSuite()
    testunit.addTest(testPrimePath("test_equal"))

    # 按照一定格式获取当前时间
    now = time.strftime("%Y-%m-%d %H-%M-%S")

    # 定义报告存放路径
    # filename = './report/result.html'
    filename = './report/蒋旺unit_test-' + now + '-result.html'
    fp = open(filename, 'wb')

    # 定义测试报告
    runner = HTMLTestRunner(stream=fp,                  # 指定测试报告文件
                        title='primePath unit test测试报告',        # 定义测试报告标题 
                        description='测试结果：')    # 定义测试报告副标题
    runner.run(testunit)    # 运行测试用例
    fp.close()  # 关闭报告文件