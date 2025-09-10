#include <iostream>
#include <cmath>

using namespace std;

int main(void) {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N, r, c;
	cin >> N >> r >> c;

	int epoch = pow(2, N - 1);
	int pos = 0, result = 0;

	r++;
	c++;

	while (epoch > 0) {
		// cout << "epoch: " << epoch << "\n";
		// cout << "col: " << c << ", row: " << r << "\n";

		if (r - epoch > 0) {
			r = r - epoch;
			// cout << "r: " << r << "\n";
			pos = pos + 2;
		}
		if (c - epoch > 0) {
			c = c - epoch;
			// cout << "c: " << c << "\n";
			pos = pos + 1;
		}
		result += pow(epoch, 2) * pos ;
		// cout << "chuck size: " << pow(epoch, 2) << ", pos: " << pos << "\n";
		N--;
		epoch = pow(2, N - 1);
		// cout << "result : " << result <<  "\n";
		pos = 0;
	}
	cout << result << "\n";
	return 0;
}