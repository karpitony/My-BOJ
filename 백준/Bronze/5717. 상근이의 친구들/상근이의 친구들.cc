#include <iostream>

using namespace std;

int main(void) {
    cin.tie(nullptr);
    cout.tie(nullptr);
    ios::sync_with_stdio(false);

    int M, F;
    while (1) {
        cin >> M >> F;
        if (M == 0 && F == 0)
            break;
        cout << M + F << "\n"; 
    }

    return 0;
}