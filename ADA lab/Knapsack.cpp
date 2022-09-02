#include<iostream>
#include<bits/stdc++.h>
#include<windows.h>
#include<time.h>
using namespace std;

int max(int a, int b) { return (a > b) ? a : b; }

int knapSack(int W, int wt[], int val[], int n)
{
    Sleep(10);
	if (n == 0 || W == 0)
		return 0;

	if (wt[n - 1] > W)
		return knapSack(W, wt, val, n - 1);
	else
		return max(
			val[n - 1]
				+ knapSack(W - wt[n - 1],
						wt, val, n - 1),
			knapSack(W, wt, val, n - 1));
}

int main()
{
	int val[] = { 60, 100, 120 };
	int wt[] = { 10, 20, 30 };
	int W = 50;
	int n = sizeof(val) / sizeof(val[0]);
	clock_t st=clock();
   cout << knapSack(W, wt, val, n);
    clock_t en=clock();
    cout<<"\n\n.........time is.........\n"<<float(en-st)/CLK_TCK;

	return 0;
}
