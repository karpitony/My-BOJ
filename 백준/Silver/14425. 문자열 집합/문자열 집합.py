import sys
input = sys.stdin.readline

N, M = map(int, input().split())
_set = set()

for _ in range(N):
    _set.add(input().strip())

cnt = 0
for _ in range(M):
    s = input().strip()
    if s in _set:
        cnt += 1
        
print(cnt)