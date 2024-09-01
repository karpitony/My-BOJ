import sys
input = sys.stdin.readline

while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    
    arr.sort()
    arr2 = [a*a for a in arr]
    if arr2[2] == arr2[0] + arr2[1]:
        print("right")
    else:
        print("wrong")