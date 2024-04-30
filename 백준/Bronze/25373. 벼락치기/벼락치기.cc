#include <stdio.h>
#include <iostream>

int main()
{
	long long int N;
	std::cin >> N;

	if(N == 1) std::cout << 1 << '\n';
	else if(N < 4) std::cout << 2 << '\n';
	else if(N < 7) std::cout << 3 << '\n';
	else if(N < 11) std::cout << 4 << '\n';
	else if(N < 16) std::cout << 5 << '\n';
	else if(N < 22) std::cout << 6 << '\n';
	else if(N < 28) std::cout << 7 << '\n';
	else
	{
		long long int middle_day = N/7;
		while(1)
		{
			if( middle_day*7 >= N) break;
			else middle_day++;
		}

		std::cout << middle_day+3 << '\n';
	}
	return 0;
}