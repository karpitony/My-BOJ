#include <iostream>
#include <vector>

using namespace std;

int main(void) {
    cin.tie(nullptr);
    cout.tie(nullptr);
    ios::sync_with_stdio(false);

    int N;
    cin >> N;
    vector<vector<char>> v(N,vector<char>(N,' '));
    
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            cin >> v[i][j];

    int K;
    cin >> K;

    if (K == 1) {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++)
                cout << v[i][j];
            cout << "\n";
        }
        return 0;
    }
    
    vector<vector<char>> v2(N,vector<char>(N,' '));
    if (K == 2) {
        for (int i = 0; i < N; i++)
            for (int j = 0; j < N; j++)
                v2[i][N-1-j] = v[i][j];
    } else if (K == 3) {
        for (int i = 0; i < N; i++)
            for (int j = 0; j < N; j++)
                v2[N-i-1][j] = v[i][j];
    }

     for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++)
            cout << v2[i][j];
        cout << "\n";
    }

    return 0;
}