#include <iostream>
#include <queue>

using namespace std;

typedef struct {
    int row;
    int col;
} Point;


char maze[101][101];
int dist[101][101];

int main(void) {
    cin.tie(nullptr);
    cout.tie(nullptr);
    ios::sync_with_stdio(false);

    int N, M;
    
    cin >> N >> M;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            cin >> maze[i][j];
        }
    }

    const int dx[] = {1, -1, 0, 0};
    const int dy[] = {0, 0, 1, -1};
    queue<Point> q;

    Point p = {0, 0};
    q.push(p);
    dist[0][0] = 1;

    while (!q.empty()) {
        p = q.front(); q.pop();
        if (p.row == N-1 && p.col == M-1)
            break;
        for (int i = 0; i < 4; ++i) {
            int new_row = p.row + dx[i];
            int new_col = p.col + dy[i];
            if (new_row >= 0 && new_row < N)
                if (new_col >= 0 && new_col < M)
                    if (maze[new_row][new_col] != '0' && !(dist[new_row][new_col] != 0)) {
                        q.push({new_row, new_col});
                        dist[new_row][new_col] = dist[p.row][p.col] + 1;
                    }
        }
    }

    cout << dist[N-1][M-1] << "\n";
    return 0;
}