
# File: readline-example-1.py
 
file = open("C:\\Users\\Gin\\Desktop\\功能自动化测试框架\\代码题\\测试用例\\case1.txt")
graph = {}
n=0
while 1:
    line = file.readline()
    if not line:
        break
    else:
        if line.strip()=="-1":
            break
        array=line.strip().split(", ")
        graph[str(n)] = array
        n = n+1
    pass # do something

print(graph)