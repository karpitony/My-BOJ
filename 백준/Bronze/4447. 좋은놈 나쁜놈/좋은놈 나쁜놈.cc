#include <iostream>
#include <string>

using namespace std;

int main() {
	int n;
	char buf[100];
	cin >> n;
	cin.getline(buf, 100); // 버퍼 비우기

	for (int i = 0; i < n; i++) {
		cin.getline(buf, 26);
		string s(buf);
		int good, bad;
		good = bad = 0;
		string::iterator it = s.begin();

		while (it != s.end()) {
			if (*it == 'G' || *it == 'g')
				good++;
			else if (*it == 'B' || *it == 'b')
				bad++;
			it++;
		}

		cout << s << " is ";
		if (good > bad)
			cout << "GOOD" << endl;
		else if (good < bad)
			cout << "A BADDY" << endl;
		else
			cout << "NEUTRAL" << endl;

	}
	return 0;
}