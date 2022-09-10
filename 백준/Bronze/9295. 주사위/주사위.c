#include <stdio.h>

int main()
{
	int T, c, v;
	scanf( "%d", &T);
	for( int i=1; i<T+1; i++)
	{
		scanf( "%d %d", &c, &v);
		printf( "Case %d: %d\n", i, c+v);
	}
}