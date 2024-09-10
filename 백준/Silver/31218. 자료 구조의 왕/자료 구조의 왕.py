import sys
input = sys.stdin.readline

n, m, Q = map(int, input().split())
zandi = [[0] * m for _ in range(n)]
remain_zandi = n * m

for _ in range(Q):
    arr = list(map(int, input().split()))

    if arr[0] == 1:
        dy, dx, y, x = arr[1], arr[2], arr[3], arr[4]
        y -= 1
        x -= 1
        
        while True:
            if not (0 <= y < n and 0 <= x < m):
                break
            
            if zandi[y][x] == 0:
                zandi[y][x] = 1 
                remain_zandi -= 1
            else:
                break
            
            if 0 <= y + dy < n and 0 <= x + dx < m:
                y, x = y + dy, x + dx
            else:
                break
        
    elif arr[0] == 2:
        y, x = arr[1] - 1, arr[2] - 1
        print(zandi[y][x])
            
    else:   # arr[0] == 3:
        print(remain_zandi)