import sys
input = sys.stdin.readline

n = int(input())
dp = [0 for _ in range(n+1)]

j = 0
while j**2 <= n:
    dp[j**2] = 1
    j += 1
    
for i in range(1, n+1):
    if dp[i] != 0:
        continue
    else:
        j = 1
        while j**2 <= i:
            if dp[i] == 0:
                dp[i] = dp[j**2] + dp[i - j**2]
            else:
                dp[i] = min(dp[i], dp[j**2] + dp[i - j**2])
            j += 1

print(dp[n]) 