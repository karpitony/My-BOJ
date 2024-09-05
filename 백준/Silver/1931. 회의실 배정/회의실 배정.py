import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    s, e = map(int, input().split())
    arr.append([s, e])

arr.sort(key=lambda x:(x[1], x[0]))

cnt = 0
end = 0
for nStart, nEnd in arr:
    if end <= nStart:
        cnt += 1
        end = nEnd

print(cnt) 
