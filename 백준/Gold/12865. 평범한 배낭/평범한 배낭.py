import sys
input = sys.stdin.readline

N, K = map(int, input().split())

total_W = 0
arr = []
for _ in range(N):
    W, V = map(int, input().split())
    total_W += W
    arr.append([W, V])

dp = [0] * (K + 1)
for W, S in arr:
    for j in range(K, W - 1, -1):
        dp[j] = max(dp[j], dp[j - W] + S)
        
print(dp[K])