import sys
input = sys.stdin.readline

N, M = map(int, input().split())
hearless = set()    # 듣도못한
watchless = set()     # 보도못한

for _ in range(N):
    name = input().strip()
    hearless.add(name)
    
for _ in range(M):
    name = input().strip()
    watchless.add(name)
    
result = list(hearless.intersection(watchless))
result.sort()

print(len(result))
for r in result:
    print(r)