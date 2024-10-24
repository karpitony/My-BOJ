#include <stdio.h>

int main(void) {
        int num = 0;
        int i = 1;
        int j;
        int reverse = 0;
        scanf("%d", &num);

        while (i > 0) {
                if (i == num)
                        reverse = 1;
                for (j = 0; j < i-1; j++)
                        printf(" ");
                for (j = 0; j < 2*(num-i)+1; j++)
                        printf("*");
                printf("\n");

                if (!reverse)
                        i++;
                else
                        i--;
        }
        return 0;
}