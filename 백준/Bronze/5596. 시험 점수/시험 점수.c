#include <stdio.h>

main()
{
	int mg[4], ms[4];
	int S=0, T=0;
	scanf( "%d %d %d %d", &mg[0], &mg[1], &mg[2], &mg[3]);
	scanf( "%d %d %d %d", &ms[0], &ms[1], &ms[2], &ms[3]);
	for( int i=0; i<4; i++)
	{
		S+=mg[i];
		T+=ms[i];
	}
	if( S>=T)
	{
		printf( "%d", S);
	}
	else
	{
		printf( "%d", T);
	}
}