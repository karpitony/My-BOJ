#include <iostream>

using namespace std;

int main(void) {
    cin.tie(nullptr);
    cout.tie(nullptr);
    ios::sync_with_stdio(false);

    int arr[8];
    for (int i = 0; i < 8; i++)
        cin >> arr[i];
    for (int i = 0; i < 8; i++)
        if (arr[i] == 9) {
            cout << "F" << "\n";
            return 0;
        }
    cout << "S" << "\n";
    return 0;
}