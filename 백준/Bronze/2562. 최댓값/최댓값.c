#include <stdio.h>

main()
{
	int num, max=0, max_num;
	for( int i=1; i<10; i++)
	{
		scanf( "%d", &num);
		if( num> max)
		{
			max = num;
			max_num=i;
		}
	}
	printf( "%d\n", max);
 	printf( "%d", max_num);
	return 0;
}