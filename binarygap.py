# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 19:56:26 2020

@author: KARTH
"""

binlist= list(str(bin(805306373)))[2:]
print(binlist)
outputlist=[]

for i,v in enumerate(binlist):
    print('i' + str(i) + str(v))
    if v =='1':
        print(v)
        outputlist.append(i+1)
  

print(outputlist)
lenlist=len(outputlist)
outputlist.reverse()
ismax=0
gap=0
for i,v in enumerate(outputlist):
     
    if (lenlist-1) > i:
        print(v)
        print(outputlist[i+1])
        gap=v-outputlist[i+1]
        print(gap)
    else:
        gap=1
    
    if gap > ismax:
        ismax=gap
    print('ismax' + str(ismax))
    


print(ismax-1)
    

