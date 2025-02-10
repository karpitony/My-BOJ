import sys
input = sys.stdin.readline

while True:
    arr = list(map(int, input().split()))
    N = arr.pop(0)
    if N == 0:
        break
    
    stack = []
    area = 0
    
    for i in range(N):
        if stack == []:
            stack.append(i)
            continue
        
        if arr[stack[-1]] < arr[i]:
            stack.append(i)
            
        # elif arr[stack[-1]] >= arr[i]:
        else:
            while stack and arr[stack[-1]] > arr[i]:
                top = stack.pop()
                if stack == []:
                    width = i
                else:
                    width = i - stack[-1] - 1
                area = max(area, arr[top] * width)
            stack.append(i) 
            
    if stack != []:
        while stack != []:
            idx = stack.pop()
            if stack == []:
                width = N
            else:
                width = N - stack[-1] - 1
            area = max(area, arr[idx] * width)
    print(area)