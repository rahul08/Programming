# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 16:14:52 2015

@author: lenovo
"""

def find_prime_by_number(n):
    list_of_prime_numbers=[]
    list_of_prime_numbers.append(2)
    while len(list_of_prime_numbers)<n:
          print len(list_of_prime_numbers)
          new_number=list_of_prime_numbers[-1]
          new_prime_found=False
          while new_prime_found==False:
                #print "yope"
                new_number=new_number+1
                #print new_number
                is_prime=2 #maybe a prime
                for each_prime in list_of_prime_numbers:
                    #print is_prime,new_number,each_prime
                    if new_number%each_prime==0:
                       is_prime=0
                if is_prime!=0:
                    new_prime_found=True
                    list_of_prime_numbers.append(new_number)
            
    return list_of_prime_numbers[n-1]
                        
         
print find_prime_by_number(10001)