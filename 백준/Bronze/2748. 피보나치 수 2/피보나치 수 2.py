import sys
input = sys.stdin.readline
 
num = int(input())
dp = [0] * (num + 1)
dp[1] = 1

for i in range(2, num + 1):
    dp[i] = dp[i-1] + dp[i-2]
    
print(dp[num])