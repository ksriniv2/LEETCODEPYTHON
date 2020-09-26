# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 19:19:05 2020

@author: KARTH
"""

#writing the code till hundreds
#input the number and convert to string as separate variable
#take mod of 100 and take the left most character
#take the last 2 digits and take mod of 10 and take the left most character
#build a dictionary from 1 to 20
#build a dictionary for base 10


numbers={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',
      13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',20:'twenty',100:'hundred'}

inpnumber=123
charnumber=str(inpnumber)

def printer(inpnumber):
    
    length=len(inpnumber)
    if length==3:
        tens=inpnumber %100
        leftmosthundred=list(inpnumber)[-1]
        leftmostten=list(inpnumber)[-2]
        leftmostone=list(inpnumber)[-3]
        ones=inpnumber%10
    
        
    

if len(charnumber)<4:
    right=int(charnumber) % 100
    leftmost=list(charnumber)[-1]
    if len(charnumber)==3:
        hundredflg=1
    outputstring=''
    outputstring=outputstring+numbers[leftmost]
    if hundredflg==1:
        outputstring=outputstring+' '+'hundred'
        
        
        

