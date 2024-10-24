#include <stdio.h>

int main(void) {
        int num = 0;
        int i, j, k;
        scanf("%d", &num);
        
        for (i = num; i >= 1; i--) {
                for (j = 0; j < num-i; j++)
                        printf(" ");
                for (k = 0; k < i*2-1; k++)
                        printf("*");
                printf("\n");
        }

        return 0;
}