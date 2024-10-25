#include <stdio.h>

int main(void) {
        int N;
        int i, j;
        
        scanf("%d", &N);
        
        for (i = 1; i <= N; i++) {
                for (j = 0; j < N-i; j++)
                        printf(" ");
                printf("*");
                if (i != N) {   
                for (j = 0; j < (i-1)*2-1; j++)
                        printf(" ");
                if (i > 1)
                        printf("*");
                
                } else {        
                        for(j =0; j < (i-1)*2; j++)
                                printf("*");
                }
                printf("\n");
        }
        return 0;
}
