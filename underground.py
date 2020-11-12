# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 17:10:41 2020

@author: KARTH
"""

#when check in

user={}
station={}

def checkin(id,station,time):
    user[id]=[station,time,None,None,None]
    
def checkout(id,station,time):

    user[id][2]=station
    user[id][3]=time
    user[id][4]=user[id][3]-user[id][1]

def avgtime(station1,station2):
    cache=[]
    for k,v in user.items():
        if user[k][0]==station1 and user[k][2]==station2:
            cache.append(user[k][4])
        

    
    
    

    print(sum(cache)/len(cache))
    


checkin(1,'A',1)
checkin(2,'A',4)
checkin(2,'B',4)
checkout(1,'B',14)
checkout(2,'B',34)
checkout(2,'C',34)

avgtime('B','C')








