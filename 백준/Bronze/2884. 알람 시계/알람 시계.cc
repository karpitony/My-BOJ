#include <iostream>

using namespace std;

int main(void) {
    cin.tie(nullptr);
    cout.tie(nullptr);
    ios::sync_with_stdio(false);

    int H, M;
    cin >> H >> M;
    if ((M - 45) < 0) {
        if (H == 0) H = 23;
        else H--;
        M = 60 + (M - 45);
    } else {
        M = M - 45;
    }
    cout << H << " " << M << "\n";

    return 0;
}