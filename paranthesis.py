# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 16:26:53 2020

@author: KARTH
"""

#start a ordered dictionary
from collections import OrderedDict
import sys
refdic={}
refdic['}']='{'
refdic[')']='('
refdic[']']='['
od=OrderedDict()
lst=[]
inpbracket='{([[])}'

#counter
counter=0
#add the new input from an array into ordered dictionary
inplist=list(inpbracket)

#run a loop of list array to get one bracket at a time
#if its in { [ ( then add 1
#if its closed bracket and its of same type as the top of stack then minus 1
for inpchar in inplist:
    
    if inpchar not in refdic:
        
        lst.append(inpchar)
        counter+=1
        print(lst)
        print(counter)
    else:
        if len(lst) > 0:
            if lst[-1]==refdic[inpchar]:
                counter-=1
                print(lst.pop())
                print(counter)
        else:
            print("Wrong formation")
            sys.exit()
        
        print(lst)
        print(counter)
#end of array there should not be any number left
        
