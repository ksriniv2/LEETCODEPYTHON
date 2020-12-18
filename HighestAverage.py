from collections import defaultdict
from math import floor

avgdict={}
input= [["Bob","-87"], ["Mike", "35"],["Bob", "52"], ["Jason","35"], ["Mike", "55"], ["Jessica", "-99"]]

for i in range(len(input)):
    if input[i][0] in avgdict:
        avgdict[input[i][0]].append(abs(int(input[i][1])))
        #sum (avgdict[input[i][0]]) / len (avgdict[input[i][0]])
    else:
        avgdict[input[i][0]]= [abs(int(input[i][1]))]
        
for k,v in avgdict.items():
    avgdict[k]=sum(avgdict[k])/len(avgdict[k])
    
for k,v in avgdict.items():
    if v==max(avgdict.values()):
        print(k +":"+ str(floor(v))) 

        
        
        
        