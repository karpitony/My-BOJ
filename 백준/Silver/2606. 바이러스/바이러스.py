import sys
from collections import deque
from dataclasses import dataclass

input = sys.stdin.readline

n = int(input())
m = int(input())
mat = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for _ in range(m):
    r, c = map(int, input().split())
    mat[r][c] = 1
    mat[c][r] = 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
queue = deque()

def bfs(count: int) -> int:
    while len(queue):
        v = queue.popleft()
        for i in range(1, n + 1):
            if not visited[i] and mat[v][i] == 1:
                visited[i] = True
                queue.append(i)
                count += 1
    return count

queue.append(1)
visited[1] = True
count = bfs(0)
print(count)