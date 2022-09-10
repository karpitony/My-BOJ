#include <stdio.h>

main()
{
	int A, sum = 0;
	for( int i=0; i<5; i++)
	{
		scanf( "%d", &A);
		sum += A;
	}
	printf( "%d", sum);
}