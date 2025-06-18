import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())
adj_mat = [[False for _ in range(N + 1)] for _ in range(N + 1)]

for _ in range(M):
    row, col = map(int, input().split())
    adj_mat[row][col] = adj_mat[col][row] =True

adj_mat_dfs_visited = [False for _ in range(N + 1)]
adj_mat_bfs_visited = [False for _ in range(N + 1)]


def adj_mat_dfs(vertex: int):
    print(vertex, end=" ")
    adj_mat_dfs_visited[vertex] = True
    for i in range(1, N + 1):
        if adj_mat[vertex][i] and not adj_mat_dfs_visited[i]:
            adj_mat_dfs(i)

def adj_mat_bfs(vertex: int):
    queue = deque()
    queue.append(vertex)
    adj_mat_bfs_visited[vertex] = True
    while len(queue):
        v = queue.popleft()
        print(v, end=" ")
        for i in range(1, N + 1):
            if adj_mat[v][i] and not adj_mat_bfs_visited[i]:
                adj_mat_bfs_visited[i] = True
                queue.append(i)


adj_mat_dfs(V)
print()
adj_mat_bfs(V)
      