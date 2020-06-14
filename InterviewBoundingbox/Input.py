# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 10:41:28 2019

@author: KARTH
"""
import numpy as np
lcount=0
ccount=0
oplist={}
lc=0
f=open("input.txt","r")
fr=f.readlines()
lflg=0
rflg=0
uflg=0
dflg=0
for x in fr:
    cc=len(x.strip())
    lc=lc+1
a = np.zeros(shape=(lc,cc))
for x in fr:
    #print(x)
    xs=x.strip()
    lst=list(xs)
    
    for element in lst:
        
        if element=='-':
            element=0
        if element=='*':
            element=1
        #print(element)
        #print(a)
       
        
        a[lcount][ccount]=element
        if ccount < len(xs):
            ccount+=1
    lcount+=1
    ccount=0
print(a)
ol=0
il=0


for ol in range(lc):
    for il in range(cc):
        
        if a[ol][il]==1:
            rflg=1
            lflg=1
            dflg=1
            uflg=1
            sflg=1
            #Left
            if il>0 and a[ol][il-1]==1:
                lflg=0
            # Right
#            if il<(cc-1) and a[ol][il+1]==1 :
#                rflg=1
            # Down
            if ol < (lc-1) and a[ol+1][il]==1:
                dflg=0
            #up
#            if ol >0 and a[ol-1][il]==1 and rflg==0:
#                uflg=1
            #spl
            if ol >0 and a[ol-1][il]==1 and il<(cc-1) and a[ol][il+1]==1:
                sflg=0
            
            
            flg=rflg*lflg*dflg*uflg*sflg
            oplist[str(ol+1)+":"+str(il+1)]=flg
print(oplist)
            
            
            


                  
                  
                  
              
          
          
          
                
      



