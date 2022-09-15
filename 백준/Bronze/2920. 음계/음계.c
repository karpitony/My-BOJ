#include <stdio.h>

int main()
{
    int	arr[8], num=0;
    for( int f=0; f<8; f++)
	{
		scanf( "%d", &arr[f]);	
		if( f>=1)
		{
			if( arr[f]-arr[f-1]==1) num+=1;
			else if( arr[f]-arr[f-1]==-1) num-=1;
			else num+=0;
		}
	}
	if( num==7) printf( "ascending");
	else if( num==-7) printf( "descending");
	else printf( "mixed");
	return 0;
}