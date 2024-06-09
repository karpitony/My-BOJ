A, B = map(int, input().split())
if A==1 and B==1:
    print(1)
else:
    arr = list()
    arr.append(0)
    for i in range(B):
        for j in range(i):
            arr.append(i)

    result = sum(arr[A:B+1])
    print(result)