# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 06:02:52 2020

@author: KARTH
"""
##No Recursion DFS
##Check only right and down and modify the current to a different flag

arr=[[1,1,1,0],
     [0,0,0,0],
     [1,0,0,1],
     [1,0,0,0],
     [1,0,1,0]
     ]



outer=len(arr) 
inner=len(arr[0]) 
islandcounter=1
for i in range(outer):
    #islandcounter+=1
    for j in range(inner):
        #print("i :" + str(i))
        #print("j :" + str(j))
        if arr[i][j]==1:      
            islandcounter+=1
            #print(islandcounter)
            arr[i][j]=islandcounter
            #print(arr)
            if j < (inner-1):            
                if arr[i][j+1]==1:
                    arr[i][j+1]=islandcounter
                    #print(arr)
            if i < (outer-1):
                if arr[i+1][j]==1:
                    arr[i+1][j]=islandcounter
                    #print(arr)
        elif arr[i][j]>1:
            if j < (inner-1):
                if arr[i][j+1]==1:
                    arr[i][j+1]=arr[i][j]
                if i < (outer-1):
                    if arr[i+1][j]==1:
                        arr[i+1][j]=arr[i][j]
print(islandcounter)
            





