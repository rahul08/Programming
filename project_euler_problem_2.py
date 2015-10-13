sum=0
x1=1
x2=1
x=x1+x2
while x<4000000:
    print x
    if x%2==0:
        sum=sum+x
    x1=x2
    x2=x
    x=x1+x2
print 'sum is'
print sum
   

    
