#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int N, M;
    cin >> N >> M;

    int player[N][M];
    int score[N] = {0};

    for (int i = 0; i < N; i++) {
        for (int k = 0; k < M; k++) cin >> player[i][k];

        sort(player[i], player[i] + M);
    }

    for (int i = 0; i < M; i++) {
        int max_num = -1;
        for (int k = 0; k < N; k++) {
            if (player[k][M - (i + 1)] > max_num) max_num = player[k][M - (i + 1)];
        }

        for (int k = 0; k < N; k++) {
            if (player[k][M - (i + 1)] == max_num) score[k]++;
        }
    }

    int max_score = *max_element(score, score + N);  // 최대 점수 찾기


    for (int j = 0; j < N; j++) {
        if (score[j] == max_score) {
            cout << j + 1 << " ";
        }
    }
    cout << endl;

    return 0;
}