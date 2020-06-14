# -*- coding: utf-8 -*-
"""
Created on Wed May 27 16:13:54 2020

@author: KARTH
"""

arr=[0,1,0,2,1,0,1,3,2,1,2,1]
#print(arr[3:])

#We need to identify between Empty, Filled, Solid blocks
#Assume that the building comes up from water one level at a time
#As a standard practice ignore all the left most, right most and the initial 0 and last 0s

#Get the max level
#Reduce the input by max level -1
#Run the filling method and keep a count and modify the input array
#For each block, check whether the left hand is greater and fill to its level
#Repeat
arrlevel=[]
maxlevel=max(arr) -1
#print(maxlevel)
fillercount=0
o=0
i=0
rightsum=0
while o <= (max(arr) -1):
    print("level:" + str(o))
    for i in arr:
        
        if i-maxlevel > 0:
            arrlevel.append(1)
        else:
            arrlevel.append(0)
        print(arrlevel)
            
    for count,i in enumerate(arrlevel):
        #print(i)
            #print("count" + str(count))
        #if arrlevel[count -1] >0:
            for rs in arrlevel[(count+1):]:
                #print(rs)
                rightsum=rightsum+rs
            #print("rightsum" + str(rightsum))
                #print("count" + str(count))
                #print("i" + str(i))
            if rightsum>0:
                print(arrlevel[count])
                if arrlevel[count]<arrlevel[count-1] and  count>0:
                    print("inside")
                    #print("fillercount" + str(arrlevel[count-1] - arrlevel[count]))
                    #if arrlevel[count] = max(arrlevel[count+1:])
                    if (arrlevel[count-1] - arrlevel[count]) ==1:
                        
                        fillercount=fillercount+ (arrlevel[count-1] - arrlevel[count])
                        arrlevel[count]=1
                    print("fillercount" +str(fillercount))
            rightsum=0
    print("fillercount" + str(fillercount))
    
    o+=1
    arrlevel=[]
    maxlevel-=1
    
                
            
            
            
            
        
        

        
        
    

