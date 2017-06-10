from primePath import doTest
from compareFile import IsHashEqual
import unittest

class TestFile(unittest.TestCase):
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
 
if __name__ == '__main__':
    unittest.main()
 