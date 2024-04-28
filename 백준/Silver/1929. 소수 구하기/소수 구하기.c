#include <stdio.h>

int is_prime(int num)
{
	if(num<2) return(1);
	
	int k=2;
	while(k<=(num/k))
	{
		if(num%k==0) return(1);
		k++;
	}
	return(0);
}

int main() {
	int M, N;
	scanf("%d %d", &M, &N);
	
	for(int i=M; i<N+1; i++) {
		if(is_prime(i)==0){
			printf("%d\n", i);
		}		
	}
}