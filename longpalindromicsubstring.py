# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 13:42:58 2020

@author: KARTH
"""

#long palindromic substring

#obtain the input list of string
#create a dictionary of key as each character and value as a list with indexes of each entry of same character appended
#if a character has multiple occurances those specific indexes should be the start and end point of palindrome
#by this way we can ignore various entry points or sequential check with in string
#once we get to the entry point till the next point compare the string and its reverse to see whether its matching, if its then add them to palindrome list
#finally get the longest length of string in palindrome list