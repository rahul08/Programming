#include <iostream>
#include <string>


int main()
{
    int a = 339;

    char b = a;

    char c = (char)a;

    int d = (int)b;

    int e = a & 0xff;
    std::string s = std::to_string(a);
    char const *pchar = s.c_str();
    std::cout << a << " " << b << " " <<pchar<<" "<< c << " " << d << " " << e << std::endl;
}




