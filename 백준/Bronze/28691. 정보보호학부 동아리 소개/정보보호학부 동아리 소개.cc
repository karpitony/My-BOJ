#include <iostream>
#include <string>
#include <map>

using namespace std;

int main(void) {
    cin.tie(nullptr);
    cout.tie(nullptr);
    ios::sync_with_stdio(false);

    map<char, string> m = {
        {'M', "MatKor"},
        {'W', "WiCys"},
        {'C', "CyKor"},
        {'A', "AlKor"},
        {'$', "$clear"}
    };
    char c;
    cin >> c;
    cout << m[c] << "\n";

    return 0;
}