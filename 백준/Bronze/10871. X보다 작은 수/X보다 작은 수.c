#include <stdio.h>

int main(void) {
        int N, X, i;
        int arr[10000];

        scanf("%d %d", &N, &X);
        for (i = 0; i < N; i++)
                scanf("%d", &arr[i]);

        for (i = 0; i < N; i++)
                if(arr[i] < X)
                        printf("%d ", arr[i]);

        return 0;
}
