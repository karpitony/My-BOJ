import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(input().strip()))
K = int(input())

def charToNum(c: str) -> int:
    if '0' <= c <= '9':
        return int(c)
    else:
        return ord(c) - 55
    
def numToChar(n: int) -> str :
    if 0 <= n <= 9:
        return str(n)
    else:
        return chr(n + 55)

weight = [0] * 36  
for number in arr:
    length = len(number)
    for idx, c in enumerate(number):
        num = charToNum(c)
        weight[num] += 36**(length - (idx + 1))
        
change = []
for i in range(36):
    if weight[i] > 0:
        change.append([(35 - i) * weight[i], i])


change.sort(reverse=True)

for i in range(min(K, len(change))):
    _, num = change[i]
    for number in arr:
        for j in range(len(number)):
            if charToNum(number[j]) == num:
                number[j] = 'Z'

total_sum = 0
for number in arr:
    length = len(number)
    for idx, c in enumerate(number):
        num = charToNum(c)
        total_sum += num * (36**(length - idx - 1))

result = []
if total_sum == 0:
    print(0)
else:
    while total_sum > 0:
        result.append(numToChar(total_sum % 36))
        total_sum //= 36
    result.reverse()
    print("".join(result))