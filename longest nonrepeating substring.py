# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 15:50:22 2020

@author: KARTH
"""

#longest substring without repeating characters

#input the string

#when the character already exists in dictionary, complete the array of string
#clean up the dictionary and start again
#find the max length of string

inpstr="abcdabcbb"
cache={}
optlist=[]
subnonrepeat=""
#take each character at a time and put in dictionary and add to array of string
for i,value in enumerate(list(inpstr)):
    if value not in cache:
        cache[value]=i
        subnonrepeat=subnonrepeat+value
    else:
        optlist.append(subnonrepeat)
        subnonrepeat=""
        cache.clear()
        cache[value]=i
        subnonrepeat=subnonrepeat+value

print(sorted(optlist,key=len)[-1])

    
        
    
    