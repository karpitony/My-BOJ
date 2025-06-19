import sys
input = sys.stdin.readline

N = int(input())
map_arr = [list(map(int, input().strip())) for _ in range(N)]
movement = [(0, 1), (0, -1), (1, 0), (-1, 0)]

visited = [False for _ in range(N*N)]

def dfs(v: tuple[int, int], count:int) -> int:
    if map_arr[v[0]][v[1]] == 1 and not visited[v[0]*N + v[1]]:
        visited[v[0]*N + v[1]] = True
        count += 1
        for m in movement:
            new_row = v[0] + m[0]
            new_col = v[1] + m[1]
            if new_row >= 0 and new_row < N:
                if new_col >= 0 and new_col < N:
                    count = dfs((new_row, new_col), count)
    return count

house = list()
for row in range(N):
    for col in range(N):
        if map_arr[row][col] == 1 and not visited[row*N + col]:
            count = dfs((row, col), 0)
            house.append(count)
            
print(len(house))
house.sort()
for h in house:
    print(h)