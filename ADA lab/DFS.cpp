#include<iostream>
#include<bits/stdc++.h>
#include<windows.h>
#include<time.h>
using namespace std;

class Graph
{

public:
    map<int,bool> visited;
    map<int,list<int>> adj;

    void addEdge(int v,int w)
    {
        adj[v].push_back(w);
    }

    void DFS(int v)
    {
        visited[v]=true;
       cout<<v<<" ";
        Sleep(10);
        for(auto i:adj[v])
        {
            if(!visited[i])
                DFS(i);
        }
    }
};

int main()
{
    cout<<"write n : ";
    int n;
    cin>>n;
        Graph g;
    for(int i=1;i<=n;i++)
    {
        int v1=i;
        int v2=rand()%n;
        g.addEdge(v1,v2);
    }

    clock_t st=clock();
    g.DFS(2);
    clock_t en=clock();
    cout<<"\n\n.........time is.........\n"<<float(en-st)/CLK_TCK;

    return 0;
}

