for _ in range(int(input())):
    arr = list(map(int, input().split()))
    arr2 = []
    for i in range(9): 
        if arr[i] != 0:
            for _ in range(arr[i]):
                if i == 5:
                    arr2.append(9)
                else:
                    arr2.append(i+1)
    
    arr2.sort(reverse=True)
    arr_len = len(arr2)
    result = [0] * len(arr2)
    
    left = 0
    right = len(arr2) - 1
    isLeftTurn = True  # True면 왼쪽에, False면 오른쪽

    for num in arr2:
        if isLeftTurn:
            result[left] = num
            left += 1
        else:
            result[right] = num
            right -= 1
        isLeftTurn = not isLeftTurn

    for r in result:
        print(r, end=" ")
    print()