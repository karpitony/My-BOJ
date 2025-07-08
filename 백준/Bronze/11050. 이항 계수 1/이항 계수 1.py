import sys
input = sys.stdin.readline

N, K = map(int, input().split())
 
num = max(N, K)
dp = [0 for _ in range(num + 1)]
dp[1] = 1

for i in range(2, num + 1):
    dp[i] = dp[i-1] * i
    
try :
    print(int(dp[N] / (dp[K] * dp[N - K])))
except (ZeroDivisionError):
    print(1)