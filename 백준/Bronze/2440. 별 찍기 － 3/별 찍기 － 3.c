#include <stdio.h>

int main()
{
	int N;
	scanf( "%d", &N);
	for( int i = N; i>0; i--) 
	{
		for( int f = i; f>0; f--) printf( "*");
		printf( "\n");
	}
}