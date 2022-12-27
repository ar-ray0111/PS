#include<iostream>
#include<string>
using namespace std;
string rev(string name);


int main()
{
    string name;
    cout << "Enter string:";
    cin >> name;
    cout << rev(name);
}

string rev(string name)
{
    int s = name.length();

    for (int i; i<s/2; i++)
    {
        char temp = name[i];
        name[i]= name[s-i-1];
        name[s-i-1]=temp;
    }
    return name;
}