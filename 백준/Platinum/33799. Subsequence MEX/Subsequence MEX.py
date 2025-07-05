import sys
input = sys.stdin.readline

DIGITS = "1234567890"

def get_MEX(x: str) -> str:
    k = len(x)
    
    if k == 1:
        return DIGITS.replace(x[0], '')
    
    result = ''
    for i in range(0, k-1):
        if x[i+1] == x[i]:
            result += DIGITS.replace(x[i], '') + x[i]
        else:
            result += DIGITS.replace(x[i], '') + x[i+1] + x[i]
    result += DIGITS.replace(x[-1], '')
    return result
        
t = int(input())
for _ in range(t):
    x = input().strip()
    print(get_MEX(x))