#include <stdio.h>
#include <iostream>

int main() {

	int N, Q;
	std::cin >> N >> Q;

	long long int days[N+1];
	for(int i=0; i<N+1; i++)
    {
        days[i] = 0;
    }
	
	for (int i=0; i<Q; i++) {

		long long int num, p, xq;
		std::cin >> num >> p >> xq;
		
		if (num == 1) {
			days[p] += xq;
		}
		else {
			long long int total = 0;
			for (int t=p; t<=xq; t++) total += days[t];
			std::cout << total << '\n';
		}
	}
}