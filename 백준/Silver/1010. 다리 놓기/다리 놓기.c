#include <stdio.h>

main()
{
	int T;
	scanf( "%d", &T);
	for( int i=0; i<T; i++)
	{
		int N, M, num=1;
		scanf( "%d %d", &N, &M);
		for( int f=1; f<=N; f++)
		{
			num*=(M-f+1);
			num/=f;
		}
		printf( "%d\n", num);
	}
}