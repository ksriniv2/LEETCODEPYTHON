# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 16:12:36 2020

@author: KARTH
"""

#triplet sum
#input the numbers as list
#sort them
#for each value in list start a two way search from left and right
#if the values are adding up to index value add all three to output list

inplst=[-1, 0, 1, 2, -1, -4]
inplstsorted=sorted(inplst)
print(inplstsorted)
optlist=[]
for i,value in enumerate(inplstsorted):
    maxidx=len(inplstsorted)-1
    lftidx=i+1
   
    while lftidx < maxidx:
         print("left index" + str(lftidx))
         print("right index" + str(maxidx))
         
            
            
         if (value + inplstsorted[lftidx] + inplstsorted[maxidx] ) < 0:
             lftidx+=1
         elif (value + inplstsorted[lftidx] + inplstsorted[maxidx] ) > 0:
             maxidx-=1
         elif (value + inplstsorted[lftidx] + inplstsorted[maxidx] ) == 0:
             optlist.append(str(value)+','+str(inplstsorted[lftidx])+','+str(inplstsorted[maxidx]))
             lftidx+=1
             maxidx-=1

            
    
            
print(set(optlist))
            
    


    

    

    
    
    

