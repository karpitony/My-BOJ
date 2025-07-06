import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    f = N
    cnt = 1
    while f > H:
        f -= H
        cnt += 1
    print(f"{f}{cnt:02d}")