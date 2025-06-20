import sys
input = sys.stdin.readline

N = int(input())
dp = [100000000000000 for _ in range(N + 1)]
dp[N] = 0

for t in range(N, 0, -1):
    if t % 2 == 0:
        dp[int(t / 2)] = min(dp[t] + 1, dp[int(t / 2)])
    if t % 3 == 0:
        dp[int(t / 3)] = min(dp[t] + 1, dp[int(t / 3)])
    dp[t - 1] = min(dp[t] + 1, dp[t - 1])
print(dp[1])
    