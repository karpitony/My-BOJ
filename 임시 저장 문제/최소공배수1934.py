'''
- 자꾸 시간초과 에러남
- 정 안되면 C로 해보기
'''


T = int(input())
ans = [0 for _ in range(T)]

for i in range(T):
    A, B = map(int,input().split())
    
    num = 0
    if A > B:
        num = A
    else:
        num = B
        
    while True:
        num += 1
        if num % A == 0 and num % B == 0:
            ans[i] = num
            break

for k in range(T):
    print(ans[k])
