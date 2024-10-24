#include <stdio.h>

int main(void) {
        int num = 0;
        int i = 1;
        int j, k;
        int reverse = 0;
        scanf("%d", &num);
        
        while(i > 0) {
                if (i == num)
                        reverse = 1;
                for (j = 0; j < i; j++)
                        printf("*");
                for (k = 0; k < (num-i)*2; k++)
                        printf(" ");
                for (j=0; j < i; j++)
                        printf("*");
                printf("\n");

                if (!reverse)
                        i++;
                else
                        i--;
        }
        return 0;
}
