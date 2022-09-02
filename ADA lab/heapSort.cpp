#include<iostream>
#include<bits/stdc++.h>
#include<windows.h>
#include<time.h>
using namespace std;
void heapify(int arr[], int N, int i)
{	int largest = i;
	int l = 2 * i + 1;
	int r = 2 * i + 2;
	if (l < N && arr[l] > arr[largest])
		largest = l;
	if (r < N && arr[r] > arr[largest])
		largest = r;
	if (largest != i) {
		swap(arr[i], arr[largest]);
		heapify(arr, N, largest);
	}
}

void heapSort(int arr[], int N)
{

	for (int i = N / 2 - 1; i >= 0; i--)
		heapify(arr, N, i);
		Sleep(10);
	for (int i = N - 1; i > 0; i--) {
		swap(arr[0], arr[i]);
		heapify(arr, i, 0);
	}
}

void printArray(int arr[], int N)
{
	for (int i = 0; i < N; ++i)
		cout << arr[i] << " ";
	cout << "\n";
}

int main()
{
	int arr[] = { 12, 11, 13, 5, 6, 7 ,2,5,6,1,4,6,7,100,12,134};
	int N = sizeof(arr) / sizeof(arr[0]);
	    clock_t st=clock();
   heapSort(arr, N);
    clock_t en=clock();
	cout << "Sorted array is \n";
	printArray(arr, N);
	cout<<"\n\n.........time is.........\n"<<float(en-st)/CLK_TCK;
}
