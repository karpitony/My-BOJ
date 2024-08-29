n, m = map(int, input().split())
arr = []
cnt = 0

for _ in range(n):
    P, L =  map(int, input().split())
    mile = list(map(int, input().split()))
    if P < L:
        arr.append(1)
    else:
        mile.sort(reverse=True)
        arr.append(mile[L-1])

arr.sort()
for a in arr:
    m -= a
    if m >= 0:
        cnt += 1
    else:
        break
    
print(cnt)