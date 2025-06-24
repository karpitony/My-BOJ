#include <iostream>

using namespace std;

int main(void) {
    cin.tie(nullptr);
    cout.tie(nullptr);
    ios::sync_with_stdio(false);

    int A, B, C, result;
    cin >> A >> B >> C;
    cout << A + B - C << "\n";

    result = 0;
    if (B % 1000 != B) {
        result = result + A * 10000;
    } else if (B % 100 != B) {
        result = result + A * 1000;
    } else if (B % 10 != B) {
        result = result + A * 100;
    } else {
        result = result + A * 10;
    }

    result = result + B - C;
    cout << result << "\n";

    return 0;
}