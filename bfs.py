# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 06:59:18 2020

@author: KARTH
"""

zhmatrix=[[1,0,0,0],[0,0,0,0],[0,0,0,0]]
chmatrix=[[1,0,0,0],[0,0,0,0],[0,0,0,0]]
rowlen=len(zhmatrix)
collen=len(zhmatrix[0])
i=0
j=0

#def bfs(mat):
#    for i in range(rowlen):
#        while j in range(collen):
#            if mat[i][j]==0:
#                if mat[i][j+1] + mat[i][j-1]+mat[i+1][j]+mat[i-1][j]>=1:
#                    mat[i][j]=1
#                    
#                    print(mat[i][j])
#                   
#    return mat
#
#print( bfs(zhmatrix))
inccol=0
deccol=0
incrow=0
decrow=0
count=0
while count<rowlen:
    for i in range(rowlen):
        for j in range(collen):
           
                 if (i+1) < rowlen:
                     incrow=i+1
                 else:
                     incrow=i
                
                 if (i-1)>=0:
                     decrow=i-1
                 else:
                     decrow=i
                     
                 if(j+1)< collen:
                     inccol=j+1
                 else:
                     incol=j
                 if(j-1)>=0:
                    deccol=j-1
                 else:
                    deccol=j
                 
                 if zhmatrix[i][j]==0:
                     if (zhmatrix[i][inccol] + zhmatrix[i][deccol]+zhmatrix[incrow][j]+zhmatrix[decrow][j]) >=1:
                        
                         chmatrix[i][j]=1
                     
                         
                 else:
                         chmatrix[i][j]=1
              
               
   
    print("End of  round" + str(count))
    zhmatrix=chmatrix
    print(zhmatrix)
    count+=1

     
             
                    

                    

                    
        
        
        