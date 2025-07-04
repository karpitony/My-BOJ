import sys
input = sys.stdin.readline

DIGITS = "0123456789"

def get_MEX(x: str) -> str:
    if len(x) == 1:
        d = int(x)
        if d == 1:                
            return "70"       
        first = str(d - 1)
        middle = "0"
        tail   = "".join(str(i) for i in range(1, d - 1))
        return first + middle + tail
    
    k = len(x)
    base = DIGITS * (k-1)
    edit_base = DIGITS
    f = x[0]
    l = x[-1]
    rest = x[1:-1]
    edit_base = edit_base.replace(l, '')
    
    front = ''.join(str(i) for i in range(int(f)-1, 0, -1))
    print(f"front : {front}")
    return front + base.replace('0', '', 1) + edit_base

t = int(input())
for _ in range(t):
    x = input().strip()
    print(get_MEX(x))
    
    
    
