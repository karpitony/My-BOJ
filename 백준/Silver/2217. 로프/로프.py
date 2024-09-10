import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

arr.sort()
max_weight = 0
for i in range(N):
    max_weight = max(max_weight, arr[i] * (N - i))

print(max_weight)