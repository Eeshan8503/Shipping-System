#include<iostream>
#include<bits/stdc++.h>
#include<windows.h>
#include<time.h>
using namespace std;

class Graph
{
    int V;
    vector<list<int>> adj;
public:
    Graph(int V)
    {
        this->V=V;
        adj.resize(V);
    }

    void addEdge(int v,int w)
    {
        adj[v].push_back(w);
    }

    void BFS(int s)
    {
        vector<bool> visited;
        visited.resize(V,false);

        list<int> l;
        visited[s]=true;
        l.push_back(s);

        while(!l.empty())
        {
            Sleep(10);
            s=l.front();
            cout<<s<<" ";
            l.pop_front();
            for(auto i:adj[s])
            {
                if(!visited[i])
                {
                    visited[i]=true;
                    l.push_back(i);
                }
            }
        }
    }
};

int main()
{

   Graph g(10);
   for(int i=1;i<=5;i++)
    {   int v2;
        cin>>v2;
        g.addEdge(i,v2);
        cin>>v2;
        g.addEdge(i,v2);
    }
    clock_t st=clock();
    g.BFS(2);
    clock_t en=clock();
    cout<<"\n\n.........time is.........\n"<<float(en-st)/CLK_TCK;

}
