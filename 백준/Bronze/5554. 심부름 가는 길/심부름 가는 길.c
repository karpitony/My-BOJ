#include <stdio.h>

int main()
{
	int num, time=0;
	for( int i=0; i<4; i++)
	{
		scanf( "%d", &num);
		time += num;
	}
	printf( "%d\n", time/60);
	printf( "%d\n", time%60);
	return 0;
}