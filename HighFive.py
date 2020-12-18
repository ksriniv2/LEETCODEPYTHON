# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 22:29:05 2020

@author: KARTH
"""
from math import floor
avgdict={}
outputlist=[]
input = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]

for i in range(len(input)):
    if input[i][0] in avgdict:
        avgdict[input[i][0]].append(abs(int(input[i][1])))
        #sum (avgdict[input[i][0]]) / len (avgdict[input[i][0]])
    else:
        avgdict[input[i][0]]= [abs(int(input[i][1]))]
print(avgdict)     
for k,v in avgdict.items():
    outputlist.append([k,floor(sum(sorted(avgdict[k],reverse=True)[:5])/5)])
    
    

print(outputlist)