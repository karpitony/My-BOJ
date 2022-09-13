#include <stdio.h>

int id(int A, int B, int C, int D, int E)
{
	return (A*A+B*B+C*C+D*D+E*E)%10;
}

main()
{
	int a, b, c, d, e;
	scanf( "%d %d %d %d %d", &a, &b, &c, &d, &e);
	printf( "%d", id(a, b, c, d, e));
	return 0;
}