import sys
input = sys.stdin.readline
N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())
cnt = 0
for size in sizes:
    if size == 0:
        continue
    else:
        cnt += size//T
        if size%T != 0:
            cnt += 1
    
print(cnt)
print(N//P, N%P)