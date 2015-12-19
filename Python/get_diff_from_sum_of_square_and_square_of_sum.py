# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 17:15:51 2015

@author: rahul08
"""
def sum_of_square(n):
    sum=0
    for i in range(n+1):
        sum=sum+ i**2
    return sum

def square_of_sum(n):
    sum=0
    for i in range(n+1):
        sum=sum+i
    return sum**2
def diff_sum_square_square_sum(n):
    sum1=square_of_sum(n)
    sum2=sum_of_square(n)
    return sum1-sum2
print diff_sum_square_square_sum(100)
print square_of_sum(10)
print sum_of_square(10)
