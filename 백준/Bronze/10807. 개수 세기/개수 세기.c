#include <stdio.h>

int main()
{
	int N, v, cnt=0;
	scanf( "%d", &N);
	int arr[N];
	for( int i=0; i<N; i++) scanf( "%d", &arr[i]);
	scanf( "%d", &v);
	for( int i=0; i<N; i++)
	{
		if( arr[i]==v) cnt+=1;
	}
	printf( "%d", cnt);	
	return 0;
}