import sys
input = sys.stdin.readline

arr = []
for _ in range(int(input())):
    X, Y = map(int, input().split())
    arr.append([X, Y])
    
arr.sort(key=lambda x:(x[0], x[1]))
for a in arr:
    print(a[0], a[1])