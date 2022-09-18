#include <stdio.h>


int main()
{
	int N, M, arr1[100][100], arr2[100][100];
	scanf( "%d %d", &N, &M);
	
	for( int i=0; i<N; i++)
	{
		for( int f=0; f<M; f++) scanf( "%d ", &arr1[i][f]);
	}
	for( int i=0; i<N; i++)
	{
		for( int f=0; f<M; f++) scanf( "%d", &arr2[i][f]);
	}
	for( int i=0; i<N; i++)
	{
		for( int f=0; f<M; f++)
		{
			arr1[i][f]+=arr2[i][f];
			printf( "%d ", arr1[i][f]);
		}
		printf( "\n");
	}	
	return 0;
}