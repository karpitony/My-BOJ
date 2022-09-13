#include <stdio.h>

long long calculation(long long A, long long B)
{
	return (A+B)*(A-B);
}

main()
{
	long long A, B;
	scanf( "%lld %lld", &A, &B);
	printf( "%lld", calculation(A, B));
}