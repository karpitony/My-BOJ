import sys
from collections import deque
from dataclasses import dataclass

input = sys.stdin.readline

n, m = map(int, input().split())
mat = list()
for _ in range(n):
    mat.append(list(map(int, input().split())))

distance_mat = [[-1 for _ in range(m)] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
queue = deque()

@dataclass
class Vertex():
    row: int = None
    col: int = None
    distance: int = None

def bfs():
    while len(queue):
        v:Vertex = queue.popleft()
        distance_mat[v.row][v.col] = v.distance
        distance = v.distance + 1
        
        for i in range(4):
            new_row = v.row + dx[i]
            new_col = v.col + dy[i]
            if new_row >= 0 and new_row < n:
                if new_col >= 0 and new_col < m:
                    if not visited[new_row][new_col] and mat[new_row][new_col] == 1:
                        visited[new_row][new_col] = True
                        queue.append(Vertex(new_row, new_col, distance))
            
for i in range(n):
    for j in range(m):
        if mat[i][j] == 2:
            queue.append(Vertex(i, j, 0))
            bfs()
            
for i in range(n):
    for j in range(m):
        if mat[i][j] == 0:
            print(0, end=" ")
        else:
            print(distance_mat[i][j], end=" ")
    print()