#include <stdio.h>
#include <iostream>
#include <algorithm>

using namespace std;


int main() {
	int N, count=0;
	cin >> N;
	int arr[N]={0};
	for (int i=0; i<N; i++) cin >> arr[i];

	for (int i=0; i<N; i++) {

		if (arr[i] != 1) {
			
			bool check = true;
			for (int k=2; k<arr[i]; k++) {
				if (arr[i]%k == 0) {
					check = false;
					break;
				}
			}
			if (check == true) count++;
		}
	}
	cout << count << '\n';

	return 0;
}