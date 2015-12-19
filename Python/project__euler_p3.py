# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 19:52:48 2015

@author: lenovo
"""
def palindrome(number):
    number=str(number)
    length_number=len(number)
    flag=1
    for k in range(length_number/2 +1) :
        
        if number[k]!=number[length_number-1-k]:
            flag=0
    return flag
            
        

def find_largest_palindrome(number_of_digits):
    """ Given the size of the input digits, it finds the largest palindrome, it can get. For eg for 2 digits numbers
    it would be 9009= 91*99 """
    palindrome_number=0
    for i in range(10**(number_of_digits-1),(10**number_of_digits)):
        for j in range(10**(number_of_digits-1),(10**number_of_digits)):
            number=i*j
            if palindrome(number)==1 and number>palindrome_number:
                palindrome_number=number
                print i,j
    return palindrome_number
    
print find_largest_palindrome(3)
    
   
    
    
    
    
    
    