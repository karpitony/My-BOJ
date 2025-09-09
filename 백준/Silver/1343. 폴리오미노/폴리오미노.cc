#include <iostream>
#include <string>

using namespace std;

int main() {
	int cnt = 0;
	char buf[100];
	cin.getline(buf, 51);
	
	string s(buf);
	string result;
	string::iterator it = s.begin();

	const char a[5] = "AAAA";
	const char b[3] = "BB";

	while(it != s.end()) {
		if (*it == 'X') {
			cnt++;
			if (cnt == 4) {
				result.append(a);
				cnt = 0;
			}
		}
		else {
			switch (cnt)
			{
				case 0:
					result.push_back('.');
					break;
				case 1:
				case 3:
					cout << -1 << "\n";
					return 0;
				case 2:
					result.append(b);
					cnt = 0;
					result.push_back('.');
					break;
				default:
					cout << -1 << "\n";
					return 0;
			}
		}
		it++;
	}
	if (cnt == 0) {
		cout << result << "\n";
	}
	else if (cnt == 2) {
		result.append(b);
		cout << result << "\n";
	}
	else {
		cout << -1 << "\n";
	}
	return 0;
}