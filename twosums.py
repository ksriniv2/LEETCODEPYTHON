# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 14:39:54 2020

@author: KARTH
"""

###two sum

#get the input in dictionary to easily search for the 2nd digit with number 
#as key and index as value

# for the target number, start from first number and move right
# if the number < target do target-number
# if the output is a key then print the index of both the numbers else slide to next number

inpnums=[2, 4, 11, 15]
target=15
inpdic={}
for k,v in enumerate(inpnums):
    if v <= target:
        inpdic[v]=k

for i,v in inpdic.items():
    srch=target-i
    if srch in inpdic:
        print(str(v) + "," + str(inpdic[srch]))
        