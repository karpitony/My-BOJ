#include <stdio.h>

int main()
{
	int sum=0; char ch[100];
	scanf( "%s", &ch);
	for( int i=0; i<100; i++)
	{
		if(ch[i]=='\0') break;
		sum+=1;
	}
	printf( "%d", sum);
	return 0;
}