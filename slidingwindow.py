# -*- coding: utf-8 -*-
"""
Created on Wed May 20 16:02:48 2020

@author: KARTH
"""
from collections import OrderedDict
ans = l = 0
#print(ans)
tree=[1,2,3,2,2]
last_index_of = OrderedDict()
last_index_of['a']=1
last_index_of['b']=2
last_index_of['c']=3
last_index_of['a']=2
#print(last_index_of)
last_index_of.move_to_end('b')
#print(last_index_of)
#print(last_index_of.popitem(last=False)[1])
#print(last_index_of)


def totalFruit(tree):
        last_index_of = OrderedDict()
        ans = l = 0
        for i, t in enumerate(tree):
            last_index_of[t] = i
            last_index_of.move_to_end(t)
            print(last_index_of)
            print(len(last_index_of))
            if len(last_index_of) > 2:
                ans = max(ans, i - l)
                print("ans :" + str(ans))
                print("i :" + str(i))
                l = last_index_of.popitem(last=False)[1] + 1
                print("l :" + str(l))
        print("i :" + str(i))
        print("l :" + str(l))
        return max(ans, i - l + 1)
print(totalFruit(tree))