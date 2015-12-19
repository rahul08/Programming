# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 11:46:23 2015

@author: lenovo
"""

def smallest_multiple(range_number):
    list_of_numbers_to_multiply=range(1,range_number+1)
    product=1    
    print len(list_of_numbers_to_multiply)
    for i in range(len(list_of_numbers_to_multiply)):
        for j in range(i):
            if list_of_numbers_to_multiply[i]%list_of_numbers_to_multiply[j]==0:
                list_of_numbers_to_multiply[i]=list_of_numbers_to_multiply[i]/list_of_numbers_to_multiply[j]
    for k in list_of_numbers_to_multiply:
        product=product*k
    return product


    

print smallest_multiple(20)
