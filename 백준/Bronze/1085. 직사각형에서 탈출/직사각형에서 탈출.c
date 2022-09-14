#include <stdio.h>

int f(int A, int B)
{
	if( A>=B-A) return B-A;
	else return A;
}

int main()
{
	int x, y, w, h;
	scanf( "%d %d %d %d", &x, &y, &w, &h);
	if( f(y,h)>=f(x,w))
    {
        printf( "%d", f(x,w));
    }
    else
    {
		printf( "%d", f(y,h));
    }
    return 0;
}