import sys
input = sys.stdin.readline

def gcd(A, B):
    big = max(A, B)
    small = min(A, B)
    if small != 0:
       return gcd(small, big % small)
    else:
        return int(big)
    
for _ in range(int(input())):
    arr = list(map(int, input().split()))
    gcd_num = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            current_gcd = gcd(arr[i], arr[j])
            if  current_gcd > gcd_num:
                gcd_num = current_gcd
    
    print(gcd_num)