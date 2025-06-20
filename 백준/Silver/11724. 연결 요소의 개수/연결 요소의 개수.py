import sys
input = sys.stdin.readline

vertex, edge = map(int, input().split())
adj_mat = [[0 for _ in range(vertex + 1)] for _ in range(vertex + 1)]

for _ in range(edge):
    u, v = map(int, input().split())
    adj_mat[u][v] = 1
    adj_mat[v][u] = 1

visited = [False for _ in range(vertex + 1)]
    
cnt = 0

def dfs(v: int):
    if not visited[v]:
        visited[v] = True
        for i in range(1, vertex + 1):
            if adj_mat[v][i] == 1:
                dfs(i)
                
for j in range(1, vertex+1):
    if not visited[j]:
        cnt += 1
        dfs(j)
            
print(cnt)