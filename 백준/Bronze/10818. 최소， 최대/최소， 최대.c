#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b)
{
    int num1 = *(int *)a;
    int num2 = *(int *)b;

    if (num1 < num2)
        return -1;
    
    if (num1 > num2)
        return 1;
    
    return 0;
}

main()
{
	int N;
	scanf( "%d", &N);
	int arr[N];
	for( int i=0; i<N; i++)
	{
		scanf( "%d", &arr[i]);
	}
	qsort(arr, sizeof(arr) / sizeof(int), sizeof(int), compare);
	printf( "%d %d", arr[0], arr[N-1]);
}