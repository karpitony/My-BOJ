import sys
input = sys.stdin.readline

T = int(input())


for _ in range(T):
    num = int(input())
    
    if num == 0:
        print("1 0")
        continue
    elif num == 1:
        print("0 1")
        continue
            
    dp_zero = [0 for _ in range(num + 1)]
    dp_one = [0 for _ in range(num + 1)]
    dp_zero[0] = 1
    dp_one[1] = 1
    
    for i in range(2, num + 1):
        dp_zero[i] = dp_zero[i - 2] + dp_zero[i - 1]
        dp_one[i] = dp_one[i - 2] + dp_one[i - 1]
    print(dp_zero[num], dp_one[num])
        
            