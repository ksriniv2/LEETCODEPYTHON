# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 14:34:02 2020

@author: KARTH
"""

#maximumsubarray sum

inparr=[-2,1,-3,4,-1,2,1,-5,4]
optarr=[]
#take one element at a time in sequence
#calculate the item + item -1 and put it in curr_sum
#if the curr_sum < 0 restart the window
#find the maximum values

for i,value in enumerate(inparr):
    if i==0 or curr_sum <0:
        curr_sum=value
    else:        
        curr_sum=curr_sum + value
        
    optarr.append(curr_sum)
print(max(optarr))
        

    

