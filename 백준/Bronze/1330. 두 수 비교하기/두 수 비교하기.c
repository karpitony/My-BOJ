#include <stdio.h>

int f(int a, int b)
{
	if( a>b) return ">";
	else if( a<b) return "<";
	else return "==";
}
main()
{
	int A, B;
	scanf( "%d %d", &A, &B);
	printf( "%s", f(A, B));
}