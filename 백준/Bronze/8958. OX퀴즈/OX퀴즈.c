#include <stdio.h>
#include <string.h>

main()
{
	int T;
	scanf( "%d", &T);
	for( int i=0; i<T; i++)
	{
		char ox[81];
		scanf( "%s", ox);
		int temp=1, sum=0;
		for( int f=0; f<strlen(ox); f++)
		{
			if( ox[f]=='O')
			{
				sum+=temp;
				temp+=1;
			}
			else
			{
				temp=1;	
			}
		}
		printf( "%d\n", sum);
	}
	return 0;
}