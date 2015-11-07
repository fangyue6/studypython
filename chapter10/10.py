#!/usr/bin/python
# coding: utf-8
import sys,pprint
import copy
def function1(): 
    #import sys,pprint
    pprint.pprint(sys.path)#pprint 分行答打印
def function2(): 
    import another_hello#把hello4.py重命名为another_hello.py放到  C:\\Python27\\lib\\site-packages
    another_hello.hello()
def function_10_2_1():
    #import copy
    print dir(copy)
    print copy.__all__
    #pprint.pprint( dir(copy))
    #pprint.pprint(copy.__all__)#

def function_10_2_3():
    #print range.__doc__
    print copy.__file__
    
def function_10_3_2():
    import webbrowser
    webbrowser.open("http://www.baidu.com", True, 0)#打开浏览器
    
def function_10_3_4():
    a=set([1,2,3])
    b=set([2,3,4])
    print a.union(b)
    
    print a|b
    c=a&b
    
    print c.issubset(a)
    print c >=a
    print a.intersection(b)
    
    print a&b
    
    print a.difference(b)
    
    print a-b
    print a ^ b
    
    print a.copy()
    print a.copy is a
    
    
    
function_10_3_4()


