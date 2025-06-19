import sys
from collections import deque
from dataclasses import dataclass 

input = sys.stdin.readline

M, N = map(int, input().split())
mat = list()
movement = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for _ in range(N):
    inner_mat = list(map(int, input().split()))
    mat.append(inner_mat)

queue = deque()

@dataclass
class Point:
    row: int = None
    col: int = None
    day: int = None

for row in range(N):
    for col in range(M):
        if mat[row][col] == 1:
            p = Point()
            p.row = row
            p.col = col
            p.day = 0
            queue.append(p)

day = 0
while len(queue):
    v:Point = queue.popleft()
    day = max(day, v.day)
    for m in movement:
        new_row = v.row + m[0]
        new_col = v.col + m[1]
        if new_row >= 0 and new_row < N:
            if new_col >= 0 and new_col < M:
                if mat[new_row][new_col] == 0:
                    mat[new_row][new_col] = 1
                    p = Point()
                    p.row = new_row
                    p.col = new_col
                    p.day = day + 1
                    queue.append(p)
    
for row in mat:
    if 0 in row:
        print(-1)
        break
else:
    print(day)