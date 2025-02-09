#include <stdio.h>

int main(void)
{
	int input;
	int result = 1;
	int num;

	scanf("%d", &input);
	num = input;
    
    if (num == 0)
        printf("1\n");
    else {
	    do {
		    result = result * num;
		    num--;
	    } while(num > 0);
	    printf("%d\n", result);
    }
	return 0;
}