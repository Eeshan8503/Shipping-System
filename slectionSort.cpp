#include<iostream>
#include<bits/stdc++.h>

using namespace std;

int main()
{
    vector<int> arr={56,78,34,1,67,9,89,34,6};

    for(int i=0;i<arr.size();i++)
    {
        int low=arr[i];
        int ind=i;

        for(int j=i;j<arr.size();j++)
        {
            if(low>=arr[j])
            {
                low=arr[j];
                ind=j;
            }
        }
        int temp;
        temp=arr[i];
        arr[i]=arr[ind];
        arr[ind]=temp;

    }

    for(auto i:arr)
        cout<<i<<" ";

}
