#include <stdio.h>

main()
{
	int N;
	scanf( "%d", &N);
	for(int i=1; i<N+1; i++)
	{
		for(int f=1; f<i+1; f++)
		{
			printf("*");
		}
		printf("\n");
	}
}