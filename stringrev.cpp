#include<iostream>


void strrev(char *p)
{
    char *q, r;
    q = p;
    while (*q!='\0')
    {
        q++;
    }
    q--;
    while(q<p)
    {
        swap(*p,*q);
        p++;
        q--;
    }
}

int main()
{
    char a[10];
    printf("Enter string:");
    std::cin >> a;
    strrev(a);
    std::cout << a;
}


