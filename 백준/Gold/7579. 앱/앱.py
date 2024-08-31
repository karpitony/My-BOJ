import sys
input = sys.stdin.readline

N, M = map(int, input().split())
app = list(map(int, input().split()))
cost = list(map(int, input().split()))

max_cost = sum(cost)
dp = [0] * (max_cost + 1)
for i in range(N):
    for j in range(max_cost, cost[i] - 1, -1):
        dp[j] = max(dp[j], dp[j-cost[i]] + app[i])

for k in range(max_cost + 1):
    if dp[k] >= M:
        print(k)
        break