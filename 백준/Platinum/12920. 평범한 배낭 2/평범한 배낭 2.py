import sys
input = sys.stdin.readline
 
N, M = map(int, input().split())
items = []

for _ in range(N):
    V, C, K = map(int, input().split())
    cnt = 1
    while K > 0:
        take = min(cnt, K)
        items.append((V * take, C * take))
        K -= take
        cnt *= 2

dp = [0] * (M + 1)
for weight, satisfaction in items:
    for j in range(M, weight - 1, -1):
        dp[j] = max(dp[j], dp[j - weight] + satisfaction)

print(dp[M])