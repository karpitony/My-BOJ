#include <stdio.h>


int main()
{
	int N, max=0;
	double avg=0;
	scanf( "%d", &N);
	int arr[N];
	
	for( int i=0; i<N; i++)
	{
		scanf( "%d", &arr[i]);
		if( arr[i]>max) max=arr[i];
	}
	
	for ( int f=0; f<N; f++) 
	{
        avg+=(float)arr[f]/max*100;
    }
	
	printf( "%f", avg/N);
	return 0;
}