# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 16:39:15 2020

@author: KARTH
"""

#Critical Network
#Story: FInd the node which is not repeated in any other edges
#List the edges where the above nodes are  part

#algorithm
connections = [[0,1],[1,2],[2,0],[1,3]]
i=0

cdic={}
#take one element of array at a time, add to dictionary. reverse it and add to dictionary 
for i,value in enumerate(connections):
    #if the item already exists then increase the value count
    cdic[value[0]]=(0 if cdic.get(value[0]) is None else cdic.get(value[0]) )+1
    cdic[value[1]]=(0 if cdic.get(value[1]) is None else cdic.get(value[1]) )+1

# list the keys which one value only
print(cdic)