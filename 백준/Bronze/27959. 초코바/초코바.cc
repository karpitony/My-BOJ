#include <iostream>

using namespace std;

int main(void) {
    cin.tie(nullptr);
    cout.tie(nullptr);
    ios::sync_with_stdio(false);

    int N, M;
    cin >> N >> M;
    if (N * 100 >= M) {
        cout << "Yes" << "\n";
    } else {
        cout << "No" << "\n";
    }
}