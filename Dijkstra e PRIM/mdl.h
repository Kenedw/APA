#include <iostream>
#include <limits.h>

#ifndef __MDL_H__
#define __MDL_H__


void primMST();

void printMST(int parent[], int n, int **graph);
int minKey(int key[],int n, bool mstSet[]);
void transform(int***a,int n);

void primMST();
int printSolution(int dist[], int n);

int minDistance(int dist[],int n, bool sptSet[]);
void dijkstra(int src);
		
#endif //__MDL_H_