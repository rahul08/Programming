def get_max_prime_factor(number):
    ''' Returns the max prime factor of input integer '''

    factor=number-1
    while factor>1 :
          if number%factor==0 :
             number=factor
  
          factor =factor-1
    
    return number
