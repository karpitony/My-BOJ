#include <iostream>
#include <unordered_map>
#include <string>

using namespace std;

int main(void) {
    cin.tie(nullptr);
    cout.tie(nullptr);
    ios::sync_with_stdio(false);

    int N, M;
    string str1, str2;
    cin >> N >> M;
    unordered_map<string, string> hm;

    for (int i = 0; i < N; ++i) {
        cin >> str1 >> str2;
        hm.insert({str1, str2});
    }

    for (int j = 0; j < M; ++j) {
        cin >> str1;
        cout << hm[str1] << "\n";
    }

    return 0;
}