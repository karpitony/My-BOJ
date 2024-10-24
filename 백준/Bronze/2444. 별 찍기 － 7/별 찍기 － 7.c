#include <stdio.h>

int main(void) {
        int num = 0;
        int i=1;
        int j, k;
        int reverse=0;
        scanf("%d", &num);
        
        while (i > 0) {
                if (i == num)
                        reverse=1;

                for (j = 0; j < num-i; j++)
                        printf(" ");
                for (k = 0; k < i*2-1; k++)
                        printf("*");
                printf("\n");

                if (!reverse)
                        i++;
                else
                        i--;
        }

        return 0;
}