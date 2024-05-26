#include <iostream>
#include <algorithm>

using namespace std;

int main() {

    cin.tie(NULL);

    int N;
    cin >> N;
    long long int arr1[N];
    for (int i = 0; i < N; i++) {
        cin >> arr1[i];
    }
    
    sort(arr1, arr1 + N);

    int M;
    cin >> M;
    for (int i = 0; i < M; i++) {
        long long int num;
        cin >> num;
        if (binary_search(arr1, arr1 + N, num)) {
            cout << 1 << '\n';
        } else {
            cout << 0 << '\n';
        }
    }
}
