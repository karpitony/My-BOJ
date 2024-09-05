import sys
input = sys.stdin.readline

N = int(input())
A_arr = list(map(int, input().split()))
B_arr = list(map(int, input().split()))

A_arr.sort()
B_arr.sort(reverse=True)

ans = 0
for i in range(N):
    ans += A_arr[i] * B_arr[i]
    
print(ans)

