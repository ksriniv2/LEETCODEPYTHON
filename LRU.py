# -*- coding: utf-8 -*-
"""
Created on Fri May 22 13:02:20 2020

@author: KARTH
"""

from collections import OrderedDict
lru=OrderedDict()
capacity=2
lru.capacity=2

def get(key):
    if key not in lru:
        return -1
    else:
        lru.move_to_end(key)
        return(lru[key])


def put(key,value):
    if key in lru:
        lru.move_to_end(key)
        lru[key]=value
    elif len(lru)==capacity:
        lru.popitem(last=False)
        lru[key]=value
        lru.move_to_end(key)
    elif len(lru)<capacity:
        lru[key]=value
        lru.move_to_end(key)
    return lru.items()
        
        

print(get(3))
print(put(3,3))
print(put(4,4))
print(get(4))
print(put(2,2))

        
    
    