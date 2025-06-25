#include <iostream>

using namespace std;

int main(void) {
    cin.tie(nullptr);
    cout.tie(nullptr);
    ios::sync_with_stdio(false);

    int n1, n2, k1, k2;
    cin >> n1 >> n2 >> k1 >> k2;
    cout << n1*n2 + k1 * k2 << "\n";

    return 0;
}