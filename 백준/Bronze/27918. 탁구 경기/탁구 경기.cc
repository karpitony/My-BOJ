#include <iostream>

using namespace std;

int main(void) {
    cin.tie(nullptr);
    cout.tie(nullptr);
    ios::sync_with_stdio(false);

    int N, X = 0, Y = 0;
    char win;
    cin >> N;
    for (int i = 0; i < N; ++i) {
        cin >> win;
        if (win == 'D') {
            X++;
        } else {
            Y++;
        }

        if (abs(X - Y) >= 2)
            break;
    }   
    cout << X << ":" << Y << "\n";

    return 0;
}