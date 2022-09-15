#include <stdio.h>

int main()
{
    int N, num, sum=0;
	scanf( "%d", &N);
	for( int i=0; i<N; i++)
	{
		scanf( "%1d", &num);
		sum+=num;
	}
	printf("%d", sum);
    return 0;
}