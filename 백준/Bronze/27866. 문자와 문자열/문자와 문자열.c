#include <stdio.h>

int main()
{
	int num; char str[1000];
	scanf("%s", &str);
	scanf("%d", &num);
	printf("%c", str[num-1]);
}