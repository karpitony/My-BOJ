#include <stdio.h>

int main()
{
	int N, c, v;
	scanf( "%d", &N);
	for( int i=0; i<N; i++)
	{
		scanf( "%d %d", &c, &v);
		printf( "You get %d piece(s) and your dad gets %d piece(s).\n", c/v, c%v);	
	}
}