#include <stdio.h>

int main()
{
	char jh[1000], doc[1000];
	int jh_cnt=0, doc_cnt=0;
	scanf( "%s", &jh);
	for( int i=0; i<1000; i++)
	{
		if( jh[i]=='h') break;
		jh_cnt+=1;
	}
	fflush(stdin);
	scanf( "%s", &doc);
	for( int f=0; f<1000; f++)
	{
		if( doc[f]=='h') break;
		doc_cnt+=1;
	}
	if( jh_cnt>=doc_cnt) printf( "go");
	else printf( "no");
	return 0;
}