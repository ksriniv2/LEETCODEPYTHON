# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 17:03:52 2020

@author: KARTH
"""

#Rotting Oranges

#get the input into multi dimensional array
#find the maximum length of each row
#find the maximum length of each column
#for every iteration
#for every node which is 2, take right and below and make it 2

#continue till end of array
import copy
arr=[[2,1,1,0],
     [0,0,0,0],
     [1,0,0,1],
     [1,0,0,0],
     [1,0,1,0]
     ]
arrprev=copy.deepcopy(arr)
arrnext=copy.deepcopy(arr)
length=len(arr)
depth=len(arr[0])

outercounter=0
breakcounter=0
freshfruit=0
#print(arr)
while freshfruit<1 or breakcounter < 2:
    freshfruit=0
    for i in range(length):
        for j in range(depth):
            
            #print('i:' + str(i) + 'j:' + str(j) + ':'+str(arr[i][j]))
            if arr[i][j]>1:
                #print(arr[i][j])
                if i+1 < (depth-1):
                    arrnext[i+1][j]=arr[i][j]
                    #print(arrnext)
                    #print(arr)
                if j+1 < (length-1):
                    arrnext[i][j+1]=arr[i][j]
            if arr[i][j]==1:
                freshfruit=freshfruit+1
    outercounter=outercounter+1
    print("End of minute :" + str(outercounter))
    #print(arr)
    print(arrnext)
    if arrprev==arr:
        breakcounter=breakcounter+1
    arrprev=copy.deepcopy(arr)
    arr=copy.deepcopy(arrnext)
    
    
    
        
            