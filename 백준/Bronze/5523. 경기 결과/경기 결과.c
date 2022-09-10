#include <stdio.h>

int main()
{
	int N, A, B, A_win = 0, B_win = 0;
	scanf( "%d", &N);
	for( int i=0; i<N; i++)
	{
		scanf( "%d %d", &A, &B);
		if( A>B)
		{
			A_win += 1;
		}
		else if( B>A)
		{
			B_win += 1;
		}
	}
	printf( "%d %d", A_win, B_win);
}