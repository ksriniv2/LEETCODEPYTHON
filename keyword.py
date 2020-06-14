# -*- coding: utf-8 -*-
"""
Created on Fri May 15 09:49:53 2020

@author: KARTH
"""

keywords = ["anacell", "cetracular", "betacellular"]
reviews = [
  "Anacell provides the best services in the city",
  "betacellular has awesome services",
  "Best services provided by anacell, everyone should use anacell",
]
dic1={}


for key in keywords:
    dic1[key]=0
#
for key in keywords:
    for review in reviews:
        if key.upper() in review.upper():
            dic1[key]=dic1[key]+ 1

for k,v in sorted(dic1.items(), key=lambda item:item[1], reverse=True):
    if v>0:
        print(k)
            
            
