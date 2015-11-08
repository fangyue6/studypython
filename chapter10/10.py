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
    
def function_10_3_4_set():#集合
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

def function_10_3_4_heap():
    from heapq import *
    from random import shuffle
    data=range(10)
    shuffle(data)
    heap=[]
    for n in data:
        heappush(heap,n)
    print heap
    heappush(heap,0.5)
    print heap
    
    heappop(heap)
    heappop(heap)
    print heap

def function_10_3_4_deque():
    from collections import deque
    q=deque(range(5))
    q.append(5)
    
    q.appendleft(6)
    print q
    
    q.popleft()
    print q
    
    q.rotate(3)#从下标为3的地方开始旋转
    print q
    
    q.rotate(-1)#从第一开始旋转
    print q

def function_10_3_6_random():
    from random import *
    a=[1,2,3,4,5,6,7,8,9,0]
    print sample(a,5)#从给定序列选择给定数目的元素，同时确保元素互不相同
    
    values=range(1,11) + ' J Q K'.split()
    suits = 'diamonds clubs hearts spades'.split()
    deck = ['%s of %s' % (v,s) for v in values for s in suits]
    shuffle(deck)
    pprint.pprint(deck[:12])
    
function_10_3_6_random()


