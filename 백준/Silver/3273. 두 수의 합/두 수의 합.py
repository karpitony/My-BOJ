import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

arr.sort()
cnt = 0
left_pointer = 0;
right_pointer = n - 1;

while arr[left_pointer] != arr[right_pointer]:
    result = arr[left_pointer] + arr[right_pointer]
    
    if result > x:
        right_pointer -= 1
    elif result < x:
        left_pointer += 1
    else:
        cnt += 1
        left_pointer += 1
            
print(cnt)