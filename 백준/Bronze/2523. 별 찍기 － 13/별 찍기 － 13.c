#include <stdio.h>

int main(void) {
        int N;
        int i=1;
        int j;
        int reverse=0;

        scanf("%d", &N);
        while (i > 0) {
                if (i == N)
                        reverse = 1;
                        
                for (j = 0; j < i; j++)
                        printf("*");
                printf("\n");
                
                if(!reverse)
                        i++;
                else
                        i--;
        }

        return 0;
}