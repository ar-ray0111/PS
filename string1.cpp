#include<iostream>
#include<string>

int xstrlen(std::string name);

int main()
{
    
    
    std::string name;
    int length;
    std::cout << "Enter string:";
    std::cin >> name;
    std::cout << xstrlen(name);

}

int xstrlen(std::string name)
{
    int count = 0;
    char i;
    while (i!= '\0') 
    {
        count ++;
    }
    return count;
}