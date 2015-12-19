# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 23:19:32 2015

@author: rahul08
"""
def find_special_pythagorean_triplet(n):
    
    condition_met=False
    a=1
    while condition_met==False:
          for b in range(a,n):
              c=n-a-b
              if a**2 + b**2 == c**2:
                 condition_met=True
              if condition_met:
                  break
          if condition_met==False:
              a=a+1
    return a,b,c

print find_special_pythagorean_triplet(1000)
print 200*375*425