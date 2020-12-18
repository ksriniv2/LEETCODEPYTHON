# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 12:46:27 2020

@author: KARTH
"""
import string
import math
words = ["What","must","be","acknowledgment","shall","be"]
maxlenword=0
for i in words:
    if maxlenword < len(i):
       maxlenword=len(i)
       
print(maxlenword)
    
jstlen=16
print(len(" ".join(words)))

maxrowlen=math.ceil(len(" ".join(words))/math.ceil(len(" ".join(words))/jstlen))
print(maxrowlen)
if maxlenword > maxrowlen:
    maxrowlen=maxlenword
currlen=0
currword=""
for i in words:
    currlen+=len(i)+1
    if currlen <= maxrowlen+1:
        print(currlen)
        print(i)
        currword=(currword+" "+ i).lstrip()
        
    else:
        
        if len(i)==maxrowlen:
            currword=currword+"\n"+i+"\n"
        else:
            currword=currword+"\n"+i
            
            
        print(currlen)
        print(i)
        currlen=0

print(currword)

