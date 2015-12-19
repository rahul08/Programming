# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 11:12:48 2015

@author: lenovo
600851475143
"""

def get_max_prime_factor(number):
    ''' Returns the max prime factor of input integer '''
    number=number/2
    factor=number-2
    while number%factor != 0 and factor > 1:
          factor=factor-1
          
    
    return factor
def get_all_prime_factors(number):
    all_prime_factors=set([])
    factor1=number-1
    #print factor1
    while number%factor1 != 0 and factor1 > 1:
          factor1=factor1-1
    #print factor1
    factor2=number/factor1
    if factor2 ==1:
        all_prime_factors.add(factor1)
        return all_prime_factors
    elif factor1 ==1:
         all_prime_factors.add(factor2)
         return all_prime_factors
    else:
           
            all_prime_factors.update(get_all_prime_factors(factor1))
            all_prime_factors.update(get_all_prime_factors(factor2))
            return all_prime_factors
    
    
print get_all_prime_factors(500000000)
#print get_max_prime_factor(50000000 )