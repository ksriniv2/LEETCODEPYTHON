# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 14:54:03 2020

@author: KARTH
"""
#https://leetcode.com/problems/reorder-data-in-log-files/
logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
#log sort
numericlog=[]
alphalog=[]
finallist=[]
words=[]
#take one value from the list at time
for i in logs:
    #split them based on space
    intlst=i.split(" ")
    #if number pop and put it in another array.append
    if intlst[1].isdigit():
        numericlog.append(i)
    else:
        #if isalpha
        alphalog.append(i)
        
    #sort the array on 1 and 0    


finallist=sorted(alphalog, key=lambda x: (x.split(" ")[1][0]))
#later append the number array to the sorted array
print(finallist + numericlog)
    
    
    
        
        





