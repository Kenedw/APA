#include "mdl.h"
#include <iostream>
//Algoritimo para o problema de caminho minimo, utilizando os algoritimos gulosos, Dijkstra e PRIM

 int minKey(int key[],int n, bool mstSet[])
{
  
   int min = INT_MAX, min_index;
   
 
   for (int v = 0; v < n; v++)
     if (mstSet[v] == false && key[v] < min)
         min = key[v], min_index = v;
 
   return min_index;
}

void transform(int***a,int n)
{
    *a=new int*[n];
    for (int i = 0; i < n; ++i)
    {
        (*a)[i]=new int[n];
    }
   
 
}

void printMST(int parent[], int n, int** graph)
{
   std::cout<<"Edge   Weight"<<std::endl;
   for (int i = 1; i < n; i++)
    std::cout<<parent[i]<<" " << i << " " <<graph[i][parent[i]]<<std::endl;
}



void primMST()
{
    int n,valor;
    std::cin >> n;
    int** MAT;
    transform(&MAT,n);
    for(int i=0; i < n; ++i)
    {
     for(int j=i+1; j < n; ++j)
        {
           std::cin>>valor;
           MAT[i][j] = valor;
           MAT[j][i] = valor;
           
        }
    }
     int parent[n];
     int key[n];  
     bool mstSet[n];  
 
   
     for (int i = 0; i < n; i++)
        key[i] = INT_MAX, mstSet[i] = false;
 
     
     key[0] = 0;    
     parent[0] = -1;
 
   
     for (int count = 0; count <n-1; count++)
     {
       
        int u = minKey(key, n,mstSet);
 
     
        mstSet[u] = true;
 
       
        for (int v = 0; v < n; v++)
 
         
          if (MAT[u][v] && mstSet[v] == false && MAT[u][v] <  key[v])
             parent[v]  = u, key[v] = MAT[u][v];
     }
 
   
     printMST(parent, n, MAT);
}

int printSolution(int dist[], int n)
{
   std::cout<<"Vertex   Distance from Source"<<std::endl;
   for (int i = 0; i < n; i++)
      std::cout<< i <<" " <<dist[i]<<std::endl;;
}

int minDistance(int dist[],int n, bool sptSet[])
{
   // Initialize min value
   int min = INT_MAX, min_index;
  
   for (int v = 0; v < n; v++)
     if (sptSet[v] == false && dist[v] <= min)
         min = dist[v], min_index = v;
  
   return min_index;
}

void dijkstra(int src)
{
     int n,valor;
    std::cin >> n;
    int** MAT;
    transform(&MAT,n);
    for(int i=0; i < n; ++i)
    {
        for(int j=i+1; j < n; ++j)
            {
                std::cin>>valor;
                MAT[i][j] = valor;
                MAT[j][i] = valor;
           
            }
    }

     int dist[n];     
  
     bool sptSet[n]; 
  
    
     for (int i = 0; i < n; i++)
        dist[i] = INT_MAX, sptSet[i] = false;
  
    
     dist[src] = 0;
  
     
     for (int count = 0; count < n-1; count++)
     {
       
       int u = minDistance(dist,n , sptSet);
  
       
       sptSet[u] = true;
  
     
       for (int v = 0; v < n; v++)
  
         
         if (!sptSet[v] && MAT[u][v] && dist[u] != INT_MAX 
                                       && dist[u]+MAT[u][v] < dist[v])
            dist[v] = dist[u] + MAT[u][v];
     }
  
    
     printSolution(dist, n);
}