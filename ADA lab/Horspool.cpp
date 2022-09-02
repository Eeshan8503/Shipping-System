#include<iostream>
#include<bits/stdc++.h>
#include<windows.h>
#include<time.h>
using namespace std;

int main()
{
    string source;
    string pattern;
    int table[126];
    cout<<"write source: ";
    getline(cin,source);
    cout<<"write pattern: ";
    getline(cin,pattern);
    int m=pattern.size();
    int n=source.size();
    for(int i=0;i<26;i++)
    {
        table[i]=pattern.size();
    }
    for(int i=0;i<m;i++)
    {
        table[pattern[i]]=m-1-i;
    }



    int i=m-1;

    while(i<n)
    {
        int k=0;
        while(k<m&&pattern[m-1-k]==source[i-k])
        k++;

        if(k==m)
        {
            cout<<"found at "<<i-m+1;
            break;
        }
        else
        {
            i+=table[source[i]];
        }

    }

    cout<<"not found ";

    return 0;

}
