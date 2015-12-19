# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 16:30:13 2015

@author: lenovo
"""

sum=0;

for x in range(0,1000):
    if x % 3 == 0:
        sum=sum+x
        print x
    elif x% 5 ==0:
        sum=sum+x
        print x

        
print sum
    