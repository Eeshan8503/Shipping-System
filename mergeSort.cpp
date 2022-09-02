#include<iostream>
using namespace std;

void Merge(int left[],int right[],int arr[],int leftSize,int rightSize)
{
    int i=0;//for left
    int j=0;//for right
    int k=0;//for arr

    while(i<leftSize && j<rightSize)
    {
        if(left[i]<=right[j])
        {
            arr[k]=left[i];
            i++;
        }

        else
        {
            arr[k]=right[j];
            j++;
        }

        k++;
    }

    while(i<leftSize)
    {
        arr[k]=left[i];
        i++;
        k++;
    }

     while(j<rightSize)
    {
        arr[k]=right[j];
        j++;
        k++;
    }


}

void mergeSort(int arr[], int n)
{
    if(n==0)
        return;

    if(n==1)
        return;

    int leftSize=n/2;
    int rightSize=n-leftSize;

    int left[leftSize];
    int right[rightSize];

    //copying
    int k=0;
    for(int i=0;i<leftSize;i++)
    {
        left[i]=arr[k];
        k++;
    }

    for(int i=0;i<rightSize;i++)
    {
        right[i]=arr[k];
        k++;
    }

    //function calling

    mergeSort(left,leftSize);

    mergeSort(right,rightSize);

    Merge(left,right,arr,leftSize,rightSize);

  //  return;
}


int main()
{
    int arr[]={4,6,8,3,1,2,5};
    int n=sizeof(arr)/sizeof(arr[0]);

    for(auto i:arr)
    cout<<i<<" ";
    cout<<endl;

    mergeSort(arr,n);

    for(auto i:arr)
    cout<<i<<" ";

    return 0;
}
