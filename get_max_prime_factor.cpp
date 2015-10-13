// Example program
#include <iostream>
#include <string>

int get_max_prime_factor(int number)
{
    int factor = number -1;
    while (factor > 1)
    {
          if (number%factor ==0)
          {
             number = factor;
          }
          factor=factor-1;
    }
    return number;
}
         
int main()
{
  printf("%d \n",get_max_prime_factor(101));
  
}
